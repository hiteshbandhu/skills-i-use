# Taste: what lands and what flops

Learned the hard way across 17+ cuts for a founders' reading club (low-res WhatsApp café footage,
Hinglish chatter) and a talking-head book-notes series. Read before choosing a concept. When a
new reaction comes in, add the rule here.

## The one-line version

**Bold graphic transformation of real footage, driven by segmentation, with giant type and
energy.** Not subtle, not moody, not a tech demo.

## Landed

| Reaction | Cut | Why it worked |
|---|---|---|
| "just peak… I loved it" (benchmark) | LIVE COLLAGE | subjects lifted into stop-motion paper cut-outs on flat bold colour; a clear idea; playful; 12 fps |
| "out of the world" | BEHIND THE WORDS | giant words placed *behind* people via person mattes; reads instantly, looks expensive |
| "Damn" | YOU ARE WHAT YOU READ | people rebuilt from letters inside their mattes; concept = the subject |
| liked best early on | THIS IS RFS | kinetic poster: condensed type that fills the width, footage inside letters, taped-print photo dump on the drop |
| "nice", wanted more | doc cut (talking head) | archival photos with Ken Burns, punch-ins, lesson cards, UI demos |

## Flopped

| Reaction | Cut | Lesson |
|---|---|---|
| "Total ass" | HANDS (light trails from fingertips) | subtle overlays on normal-looking footage do not land; transform the image boldly |
| "Shitty. Forced" | MOSHPIT (datamosh, x-ray, contour sketch) | effects that exist to show off models feel forced; every effect needs an idea |
| "can't best the first one" | Netflix trailer | moody/cinematic genres lose to bold type + energy |
| "okish" | FOUND FOOTAGE (Y2K camcorder) | nostalgia filter alone is not a concept |
| "looks AI" | soft editorial recap | centred serif captions, polite placement and generic layouts read as AI-made |
| "it gets dark" | dark grade | keep footage bright; lift, don't crush |
| "looks bad" | permanent brand header | no persistent title bars; the brand appears once, at the end |

## Rules

**Concept**
- One idea per reel, about the subject. Write it in a sentence before building.
- Transform the footage itself (mattes, lifts, type interacting with people), not only overlay it.
- Use all the footage the user cares about. They noticed when the laptop clip was skipped, and they want live movement, not only stills.
- "Go ham" or "different" means a new visual language *and* new techniques. Changing the grade is not enough.

**Type**
- Condensed heavy sans (Futura Condensed ExtraBold) set to fill the width. Big, few words, punchy.
- No full stops in on-screen text. Ever.
- Type interacts with the image (inside letters, behind people, at a depth plane). Floating captions read as AI.
- Paper / red / ink (`#F1EEE6 #FF3B1F #111`) worked well; vary it per concept.

**Image**
- Bright. Contrast yes, crushed blacks no.
- Grain, paper texture, halftone and tape make it look made by hand rather than generated.
- Stop-motion frame rates (12 fps) for collage/comic; 30 fps for camera moves.

**Motion and sync**
- Every cut on a beat; drops land on kicks; a 3-frame punch-in on hard cuts.
- Motion targets must be measured (matte bbox, pose JSON, DOM rect), then verified on a zoomed frame. A ring 20 px off is noticed.

**Captions (talking head)**
- Phrase-sized chunks, keyword emphasis, well inside the safe zone (they got cut off on the user's phone once).
- Narrower than you think: max width ~860 px, baseline above y 1500.

**Sound**
- They want real music and SFX (this reversed an earlier "no SFX" preference).
- Soft audio edges: 30–60 ms crossfades, room tone under jump cuts, J/L cuts.
- SFX tied to visible events only. Mix to -14 LUFS with a static gain + limiter.

**Process**
- Ask before downloading outside assets. Flag rights risks (game audio = mute risk).
- Flag any fact you add that the speaker did not say.
- Deliver, then log the reaction in concepts.md.
