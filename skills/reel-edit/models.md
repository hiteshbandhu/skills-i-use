# On-device models: what a Mac can do for an edit

Tested on an M2 with 8 GB. Rule of thumb: one model in memory at a time, and anything over
~1B parameters is too heavy for per-frame video work.

## Built into macOS (free, no download): `scripts/vision/`

| Tool | Apple API | Output | Use |
|---|---|---|---|
| `seg` | `VNGeneratePersonSegmentationRequest` (.accurate) | person matte PNG | words behind people, glyph portraits, occlusion, clone mattes |
| `fg` | `VNGenerateForegroundInstanceMaskRequest` (macOS 14+) | any-subject matte | sticker/collage lifts of books, laptops, pens, people |
| `hand` | `VNDetectHumanHandPoseRequest` | fingertips JSON | follow labels, match cuts, trails |
| `pose` | `VNDetectHumanBodyPoseRequest` | joints JSON | skeleton graphics, motion-reactive edits |
| `flow` | `VNGenerateOpticalFlowRequest` | float32 flow fields | datamosh, motion-reactive effects (use with an idea) |
| `contour` | `VNDetectContoursRequest` | polylines JSON | line-drawing reveals |
| `depth` | Core ML + Vision | 16-bit depth PNG | 2.5D parallax, dolly zoom, depth-placed text, haze |

Also in Vision but not wrapped yet: saliency (where the eye goes, useful for auto-reframe), horizon,
trajectories, animal pose, 3D body pose, document detection, image feature prints (find similar shots).

## Downloaded models that worked

| Model | Size | Runtime | Speed (M2) | Notes |
|---|---|---|---|---|
| Depth Anything V2 Small F16 (Apple Core ML) | ~48 MB | `vision/bin/depth` | fast | Apache-2.0; compiled at runtime |
| MediaPipe face / hand / pose / selfie segmenter | 3–8 MB | Python or web tasks-vision | real-time | face blendshapes drive characters |
| faster-whisper small.en / medium | 0.5–1.5 GB | CPU int8 | ok | `transcribe.py` |
| Kokoro-82M (mlx-audio) | ~330 MB | MLX | faster than real time | needs misaki, spaCy, phonemizer-fork, espeakng-loader |
| RF-DETR base (mlx-community) | ~130 MB | mlx-vlm | ~95 ms/frame | counting/detection (`lab/mlx_detect_server.py`) |
| Florence-2 base ft 8-bit (mlx-community) | ~250 MB | mlx-vlm | 0.6–1 s | `<OD>`, `<CAPTION>`, phrase grounding = "find the X" |
| AnimeGAN2 face_paint_512_v2 / paprika | 8 MB each | PyTorch MPS | ok | restart the worker every ~40 frames (MPS leak) |
| Depth Anything V2 small (ONNX, transformers.js WebGPU) | ~50 MB | browser | real-time-ish | for live webcam toys |

## Tried and too heavy for 8 GB
- SAM3 (MLX, mxfp4): 108 s per frame. Use `fg`/`seg`, Florence grounding or SAM 2 tiny instead.
- VGGT / MASt3R (multi-view 3D) and DepthCrafter (diffusion video depth): out of memory.

## Worth adding next (fit on 8 GB)

| Model | Gives | Edit it unlocks |
|---|---|---|
| Video Depth Anything (small) | temporally stable depth | flicker-free parallax |
| CoTracker3 | track any pixel through a clip | type/stickers pinned to tables, books, walls |
| SAM 2 tiny (~39M) | click once → object masked through the clip | isolate one book/laptop for collage or recolour |
| BiRefNet / RMBG-2.0 | hair-level cut-outs | cleaner stickers than Vision |
| RobustVideoMatting | real-time matting | live green-screen-free effects |
| SEA-RAFT | sharper optical flow | better slow-mo / motion effects |
| RIFE | frame interpolation | smooth speed ramps and slow-mo from 30 fps |
| LaMa (~50M) | inpainting | remove a person or object from a shot |
| Real-ESRGAN | upscaling | rescue 478 px WhatsApp footage |
| Depth Pro (Apple) | sharp metric depth | high-quality single-shot 3D photos (slow) |
| MoGe | point cloud from one image | true 3D camera moves |
| DSINE / Metric3D | surface normals | relight footage after the fact |
| Demucs | music stems | cut exactly on the drums, duck only vocals |
| Basic Pitch | music → notes | visuals reacting to melody |
| macOS Object Capture | photos → textured 3D model | spinning 3D product/book shots |

## Training your own (under 50M parameters, on the laptop)
Feasible in MLX or PyTorch MPS: small classifiers on frozen embeddings, tiny segmentation
fine-tunes, LoRA on small vision models. For edit tooling, a frozen encoder plus a small head
almost always beats training from scratch.
