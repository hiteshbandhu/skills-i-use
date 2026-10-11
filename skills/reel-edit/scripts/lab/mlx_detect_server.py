"""Local MLX vision server (127.0.0.1:8788): RF-DETR counting + Florence-2 identify/find. POST a JPEG to /count, /identify or /find?q=thing. Needs mlx-vlm."""
import io, json, time, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
import numpy as np, cv2
from PIL import Image
from pathlib import Path
from mlx_vlm.utils import load_model, get_model_path

import re
LOCK = threading.Lock()
_det = _flo = None

def detector():
    global _det
    if _det is None:
        from mlx_vlm.models.rfdetr.processing_rfdetr import RFDETRProcessor
        from mlx_vlm.models.rfdetr.generate import RFDETRPredictor
        p = get_model_path("mlx-community/rfdetr-base-fp32")
        _det = RFDETRPredictor(load_model(Path(p)), RFDETRProcessor.from_pretrained(str(p)), score_threshold=0.4, nms_threshold=0.5)
    return _det

def florence():
    global _flo
    if _flo is None:
        from mlx_vlm import load
        _flo = load("mlx-community/Florence-2-base-ft-8bit")
    return _flo

def flo(task, img):
    from mlx_vlm import generate
    m, p = florence()
    r = generate(m, p, task, image=[img], max_tokens=320, temperature=0.0, verbose=False, skip_special_tokens=False)
    return (r.text if hasattr(r, "text") else r).replace("<s>", "").replace("</s>", "").replace("<pad>", "")

def parse_locs(txt, W, H):
    """Florence output -> [(label, [x1,y1,x2,y2])]; label carries over to following boxes."""
    out, label = [], ""
    for chunk in re.finditer(r"([^<]*)((?:<loc_\d+>){4})", txt):
        if chunk.group(1).strip(): label = chunk.group(1).strip()
        v = [int(x) for x in re.findall(r"<loc_(\d+)>", chunk.group(2))]
        out.append((label, [(v[0] + .5) / 1000 * W, (v[1] + .5) / 1000 * H, (v[2] + .5) / 1000 * W, (v[3] + .5) / 1000 * H]))
    return out

def iou(a, b):
    ix = max(0, min(a[2], b[2]) - max(a[0], b[0])); iy = max(0, min(a[3], b[3]) - max(a[1], b[1])); i = ix * iy
    u = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - i
    return i / u if u > 0 else 0

def nms(boxes, thr=0.6):
    keep = []
    for b in sorted(boxes, key=lambda b: (b[2] - b[0]) * (b[3] - b[1])):
        if all(iou(b, k) < thr for k in keep): keep.append(b)
    return keep

def count(img):
    r = detector().predict(img)
    dets = [dict(label=n, score=float(s), box=[float(v) for v in b]) for n, s, b in zip(r.class_names, r.scores, r.boxes)]
    totals = {}
    for d in dets: totals[d["label"]] = totals.get(d["label"], 0) + 1
    return dict(detections=dets, counts=totals)

def identify(img):
    W, H = img.size
    objs = [dict(label=l, box=b) for l, b in parse_locs(flo("<OD>", img), W, H)]
    cap = flo("<CAPTION>", img).strip()
    return dict(objects=objs, caption=cap)

SYN = {"people": "person", "persons": "person", "men": "person", "man": "person", "women": "person", "woman": "person", "humans": "person", "human": "person",
       "phone": "cell phone", "phones": "cell phone", "mobile": "cell phone", "mobiles": "cell phone", "glass": "wine glass", "mug": "cup", "mugs": "cup",
       "notebook": "book", "notebooks": "book", "table": "dining table", "tables": "dining table", "plant": "potted plant", "plants": "potted plant", "tv": "tv", "screen": "tv"}
def find(img, q):
    W, H = img.size; ql = q.lower().strip()
    sing = SYN.get(ql, ql[:-1] if ql.endswith("s") and not ql.endswith("ss") else ql)
    c = count(img)
    hits = [d["box"] for d in c["detections"] if sing in d["label"].lower() or d["label"].lower() in sing]
    src = "RF-DETR"
    if not hits:
        hits = [b for l, b in parse_locs(flo("<OD>", img), W, H) if sing in l.lower()]; src = "Florence-2 detect"
    if not hits:
        hits = [b for l, b in parse_locs(flo("<CAPTION_TO_PHRASE_GROUNDING>" + q, img), W, H) if (b[2]-b[0])*(b[3]-b[1]) < 0.85 * W * H]; src = "Florence-2 grounding"
    hits = nms(hits)
    return dict(query=q, matches=[dict(box=b) for b in hits], count=len(hits), source=src)

class H(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        b = json.dumps(obj).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*"); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_OPTIONS(self):
        self.send_response(204); self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS"); self.send_header("Access-Control-Allow-Headers", "Content-Type"); self.end_headers()
    def do_GET(self):
        self._send(200, dict(ok=True, models=["rfdetr-base", "florence-2-base-8bit"]))
    def do_POST(self):
        u = urlparse(self.path); q = parse_qs(u.query)
        img = Image.open(io.BytesIO(self.rfile.read(int(self.headers["Content-Length"])))).convert("RGB")
        t0 = time.time()
        try:
            with LOCK:
                res = count(img) if u.path == "/count" else identify(img) if u.path == "/identify" else find(img, q.get("q", ["object"])[0])
            res["ms"] = int((time.time() - t0) * 1000); res["size"] = img.size; self._send(200, res)
        except Exception as e:
            self._send(500, dict(error=str(e)))
    def log_message(self, *a): pass

if __name__ == "__main__":
    print("loading RF-DETR + Florence-2…", flush=True); detector(); florence()
    print("serving on http://127.0.0.1:8788", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8788), H).serve_forever()
