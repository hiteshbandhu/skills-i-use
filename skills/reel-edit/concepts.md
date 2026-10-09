# Concept log: every cut so far

Recipes are short enough to rebuild from. "Reaction" is the user's verbatim verdict where there
was one. **Append new cuts at the bottom** (concept, technique, track, reaction).

Footage for the RFS cuts: 12 WhatsApp clips at 478×850 of a founders' reading club in a café
(books, notebooks, a laptop, hands writing, a bandana speaker). Hinglish chatter, so the cuts
were music-led.

---

### 1. Documentary cut (talking head, "User Friendly" book notes)
- **Idea:** turn a UX/psychology monologue into a mini doc.
- **Build:** tight jump cuts with punch-ins; public-domain archive photos with Ken Burns moves; black lesson cards; split-screen UI demos; phrase captions with serif-italic keywords.
- **Reaction:** liked overall. Wanted more images and stock video, motion targets measured from the DOM (a ring was off), softer audio cuts, captions inside the safe zone, SFX and real music.

### 2–4. Recruit / Recap / Manifesto (first RFS set)
- Three beat-snapped shot lists from one footage pool, with natural sound under the music, and a riser plus a sub thump into the lift.
- **Reaction:** the recap "has potential". Its text looked AI (soft serif, polite placement). The dark grade was rejected.

### 5. Recap v2, book-typeset version
- Running head, chapter openers (I, II, III), a footnote naming the books on the table, a colophon end card.
- **Reaction:** still not it. That pushed things toward bold type.

### 6. THIS IS RFS (kinetic poster) ★
- **Idea:** the reel is a poster that keeps re-setting itself.
- **Build:** Futura Condensed ExtraBold lines fitted to 960 px; footage visible *inside* the letters (grayscale); red/paper/ink cards on beats (BOOKS OPEN, PENS OUT, OPINIONS LOUD); a 4-beat READ NOTE ARGUE REPEAT strobe; zooming *through* a letter into footage; a taped-print photo dump on the drop; THIS IS RFS end card cycling footage in the mask. Paper grain multiply plus overlay.
- **Track:** Mixkit "Tech House vibes". **Reaction:** liked best early on.

### 7. FOUND FOOTAGE (Y2K digicam)
- Hand-built camcorder interface (REC, timecode, battery, segmented date), CCD look, autofocus hunt, digital zoom, flash-freeze, playback mode, battery dies → TV switch-off.
- **Track:** Mixkit "Reaching Out". **Reaction:** "okish".

### 8. Netflix docuseries trailer
- Black cards, letterbox bars, bright teal-orange grade, slow motion, three synthesised BRAAAM hits, a heartbeat, a hard silence before the title, an anamorphic flare on the RFS title.
- **Track:** Mixkit "Driving Ambition" from 26.59 s. **Reaction:** "can't best the first one".

### 9. BEHIND THE WORDS ★
- **Idea:** giant words living *behind* the people.
- **Build:** Apple Vision person segmentation (`seg`), word placement measured from each head's bbox, taped prints where people break out past the border, poster DNA from cut 6.
- **Track:** Mixkit "Midnight Funk" from 8.15 s. **Reaction:** "out of the world". Only fix asked: remove full stops.

### 10. YOU ARE WHAT YOU READ ★
- **Idea:** people made of the words they read.
- **Build:** glyph portraiture inside the person mattes. Each cell is a dim tile in the pixel's colour with a bright letter on top (pure letters were too dark). Scramble-decode reveal, an all-type drop alternating colour-on-black and red-on-paper, a particle morph of the person-letters into RFS.
- **Track:** Mixkit "Just Keep Walking" from 3.78 s. **Reaction:** "Damn". Asked to include the laptop clip and more live movement.

### 11. HANDS ✗
- Vision hand-pose (`hand`) driving long-exposure light trails from the fingertips; labels that follow the hands; match cuts solved by fingertip position; pen-tip tracking as the darkest thick blob; a script "rfs" written by the nib; sound sonified from finger speed.
- **Track:** Mixkit "Delayed Flight". **Reaction:** "Total ass". Subtle overlays don't land.

### 12. LIVE COLLAGE ★★ (benchmark)
- **Idea:** the meetup as a living paper collage.
- **Build:** Vision subject lift (`fg`) on laptop, book, pen and people → sticker cut-outs with a white edge and drop shadow on flat bold colour; paper grain, torn paper and halftone; 12 fps stop-motion; copy LOG OFF / PICK UP / A BOOK / THEN TALK IT OUT; a Warhol grid on the drop; ends on RFS behind the bandana speaker. Paper-slap SFX.
- **Track:** Mixkit "Tech House vibes" from 6.966 s. **Reaction:** "just peak… I loved it".

### 13. Comic page
- `fx/comic.py` look (bilateral, posterise, halftone, ink lines plus a matte outline) on one live comic page, moved through with a guided-view camera; a clone panel (ONE FOUNDER. THREE OPINIONS.); SFX lettering; a page turn; an RFS #01 cover. Reaction not recorded.

### 14. CLONE THE ROOM
- **Idea:** one founder, four opinions → zero agreement.
- **Build:** `fx/camtrack.py` (ORB on the background with people masked out) and `fx/clone.py` (clones from other moments of the same clip, locked to the room, far clones occluded by the real people, a contact shadow on near clones); each clone's voice panned to his side. Captions ONE FOUNDER → FOUR → ZERO AGREEMENT. Reaction not recorded (the user picked this idea themselves).

### 15. MOSHPIT ✗
- Optical-flow datamosh (`flow` + remap), x-ray strobe with neon skeletons (`pose`), a contour scan-line sketch intro (`contour`), a neon RFS.
- **Track:** "Midnight Funk" again. **Reaction:** "Shitty. Forced". These were tech showcases with no idea behind them.

### 16. GTA San Andreas mission
- Loading screen, mission title, a detailed HUD (weapon roundel, bars, money, stars, rotating radar), objectives, skill popups, a mission marker, a book pickup, cutscene subtitles, MISSION PASSED with an *original* synth fanfare (`sfx.fanfare`). The CJ "here we go again" line was downloaded with consent and flagged as Rockstar audio (mute risk). Free Pricedown font. The user asked for detailed, well-spaced assets.
- **Track:** Mixkit #431 (92 BPM G-funk-ish) from 10.0 s.

### 17. DEEPER (2.5D parallax)
- **Idea:** MOST CONVERSATIONS STAY ON THE SURFACE → OURS GO DEEPER.
- **Build:** Depth Anything V2 Small via Core ML (`depth`), `fx/parallax.py` push/orbit/dolly zoom, text at depth planes occluded by nearer people, haze; a flat desaturated intro becomes 3D on the drop.
- **Track:** Mixkit #282 from 9.0 s.

### 18. Talking book (demo)
- MediaPipe face landmarks and blendshapes drive a book-head character, lip-synced to a Kokoro-82M (mlx-audio) voice. 7 s demo.

### 19. Anime OP (stopped unfinished)
- AnimeGAN2 face_paint_512_v2 / paprika on face crops plus a cel-shade pass. MPS leaked memory (4.4 GB on 8 GB). Fix: restart the worker every ~40 frames and call `torch.mps.empty_cache()`. The user stopped it: "enough for today".

---

## Ideas not yet built
- Video Depth Anything for flicker-free parallax · CoTracker3 to pin type/stickers to surfaces ·
  SAM 2 tiny click-to-track any object · RIFE speed ramps · LaMa object removal · Demucs stems for
  drum-exact cuts. See models.md.
