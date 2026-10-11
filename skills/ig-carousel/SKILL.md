---
name: ig-carousel
description: >
  Designs and renders Instagram carousels (4:5 slides) as one continuous panorama that is
  sliced into slides: sticker cut-outs from photos or video stills, bold type, tape, torn
  paper and halftone that bleed across slide edges, a hook slide first and a single CTA on the
  last slide. Spec-driven renderer, no design app needed. Triggers on "make a carousel",
  "instagram carousel", "swipe post", "turn this video into a carousel", "carousel with a CTA",
  "slides for instagram".
---

# IG Carousel: a swipe post that ends in one ask

You design the carousel, render it from a JSON spec, look at it, fix it, and deliver numbered
slides. Everything runs locally.

**Supporting files:**
- [principles.md](principles.md): carousel structure, hook and CTA rules, layout and safe zones, a fairness checklist for real people
- [scripts/carousel.py](scripts/carousel.py): the renderer (read the docstring for the spec format)
- [examples/spec.example.json](examples/spec.example.json): a neutral 5-slide spec to copy

**Scripts:** `carousel.py` reads your spec and images and writes JPEGs into the out dir you pass. Nothing else.

Output: `{SKILL_OUTPUT_DIR}/ig-carousel/<project>/`: `spec.json`, `stickers/`, `slide_01.jpg…`, `sheet.jpg`. See [../OUTPUT.md](../OUTPUT.md).

---

## Step 1: Brief
| Setting | Default |
|---|---|
| Slides | 5–8 (Instagram allows up to 20; fewer, stronger slides win) |
| Size | 1080×1350 (4:5) |
| Goal | one action, stated on the last slide only |
| Source | photos, or stills pulled from video |
| Copy | about 2–4 words of headline per slide, no full stops |

Ask only what changes the post: **what is the single CTA** (comment a keyword, DM, link in bio,
save), and whether there are people who must not appear.

## Step 2: Story before pixels
Write the slide list as one line each: **hook → 3–6 beats that build → CTA**. The hook must work
alone in the feed. Each beat is one idea with one visual. The last slide repeats the promise
and gives exactly one action. See principles.md.

## Step 3: Make stickers
Pick stills with clear subjects. Cut them out with any matting tool, e.g. the `reel-edit`
skill's `vision/bin/fg` (Apple Vision subject lift, macOS) or rembg. One PNG matte per still
(white = keep). Crop the matte when a prop steals focus. Give each person no more than one
appearance unless the brief says otherwise.

## Step 4: Spec and render
1. Copy `examples/spec.example.json`. Panorama x runs across all slides (slide i = `[i*1080, (i+1)*1080)`).
2. Put at least one element across every seam (a torn strip, tape, a sticker or a pen) so the swipe feels continuous.
3. `python3 scripts/carousel.py spec.json out/`
4. **Open `out/sheet.jpg` and the hook and CTA slides at full size.** Check:
   - text inside the safe zone
   - nothing important cut by a seam
   - no headline clipped by an overlapping element
   - faces not covered
   - CTA legible at thumbnail size

   Fix the spec and re-render. Usually 2–3 rounds.

## Step 5: Deliver
Send the slides in order with a 3-line note: slide order, the CTA and what to do when people
respond, plus a suggested caption that repeats the CTA. If the CTA promises something (an invite, a link), tell
the user they must actually follow up.

## Hard rules
- One CTA, last slide only. No "follow, like, share and comment" lists.
- Hook slide: big type, a reason to swipe, a swipe cue.
- No full stops in headlines. Bold, few words.
- Never cover a face with type or tape; equal prominence for people in group content.
- Ask before downloading outside assets (fonts, photos); state licences.
- Keep personal details about the people or project out of any shared or public file.
