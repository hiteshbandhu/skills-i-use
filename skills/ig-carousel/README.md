# IG Carousel

Designs and renders Instagram carousels as **one continuous panorama** sliced into 4:5 slides.
Sticker cut-outs, bold type, tape, torn paper and halftone bleed across slide edges so people
keep swiping. The deck opens on a hook and ends on a single CTA.

Output: `./skill-outputs/ig-carousel/<project>/`

## Requirements
- Python 3 with `numpy` and `pillow`
- Fonts of your choice (macOS system fonts work out of the box; set paths in the spec)
- Cut-out mattes for stickers from any tool: Apple Vision subject lift (see `reel-edit` → `vision/bin/fg`), rembg, Photoshop, etc.

## Scripts
**Read before running.** `scripts/carousel.py spec.json out_dir` reads the spec and the images
it references and writes `slide_NN.jpg` and `sheet.jpg` into `out_dir`. Nothing else.

## Usage
```
@ig-carousel turn these 6 photos into a carousel that ends with "comment GUIDE"
@ig-carousel make a sticker-collage carousel from stills of this video, CTA: link in bio
```

## Files
| File | For |
|---|---|
| `SKILL.md` | workflow: brief → story → stickers → spec/render/QA → deliver |
| `principles.md` | structure, CTA rules, layout and safe zone, real-people checklist |
| `scripts/carousel.py` | spec-driven renderer: sticker, text, label, tape, torn, bubble, dots, arrow, pill |
| `examples/spec.example.json` | neutral 5-slide starting spec |
