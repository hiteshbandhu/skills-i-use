# Edit recipes

A catalogue of edit styles this skill can build, each written short enough to rebuild from. Use
it to pick a direction that is *different* from the last cut. Keep your own project history
(what you made, for whom, how it landed) in a private file outside this repo; see SKILL.md, Step 7.

Legend: **Idea** = the concept in one line · **Build** = techniques and tools · **Watch** = known traps.

---

### Documentary cut (talking head)
- **Idea:** turn a monologue into a mini documentary.
- **Build:** tight jump cuts with punch-ins; public-domain archive photos with Ken Burns moves; black lesson cards; split-screen UI demos; phrase captions with one serif-italic keyword.
- **Watch:** measure UI targets from the DOM (a ring a few px off is noticed); 30–60 ms audio crossfades; captions well inside the safe zone.

### Kinetic poster
- **Idea:** the reel is a poster that keeps re-setting itself on the beat.
- **Build:** condensed heavy type fitted to the full width; footage visible *inside* the letters (canvas `source-in`); flat-colour cards on beats; zoom *through* a letter into footage; a taped-print photo dump on the drop; paper grain.

### Words behind people
- **Idea:** giant words live *behind* the people in the shot.
- **Build:** person mattes (`vision/seg`); the word goes over the footage, then the person is re-drawn through the matte; placement measured from head boxes; prints that people "break out of".

### Glyph portraits
- **Idea:** people made of letters.
- **Build:** inside the person matte, each cell is a dim tile in the pixel's colour with a bright glyph on top (pure glyphs read too dark); scramble-decode reveal; particle morph of the letters into a logo.

### Live collage
- **Idea:** the scene as a living paper collage.
- **Build:** subject lifts (`vision/fg`) on objects and people → sticker cut-outs with a white edge and drop shadow on flat bold colour; paper grain, torn paper, halftone; 12 fps stop-motion; a grid repeat on the drop.

### Comic page
- **Build:** `fx/comic.py` (bilateral smoothing, posterise, halftone, ink lines plus a matte outline) on one live page moved through with a guided-view camera; SFX lettering; a page turn; a cover.

### Multiplicity ("clone the room")
- **Idea:** one person, several opinions.
- **Build:** `fx/camtrack.py` (ORB on the background with people masked out) and `fx/clone.py` (clones from other moments of the same clip, locked to the room, far clones occluded by the real people, contact shadow on near clones); each clone's voice panned to its side.

### Docuseries trailer
- **Build:** black cards, letterbox bars, a bright teal-orange grade, slow motion, synthesised BRAAAM hits (`sfx.braam`), a heartbeat, a hard silence before the title, an anamorphic flare.
- **Watch:** moody genres can lose to bold, energetic type. Keep the grade bright.

### Camcorder / found footage
- **Build:** a hand-built camera interface (REC, timecode, battery, segmented date), CCD look, autofocus hunt, digital zoom, flash-freeze, playback mode, battery-dies TV switch-off.
- **Watch:** a nostalgia filter alone is not a concept.

### Light trails from hands
- **Build:** Vision hand pose (`vision/hand`) → long-exposure fingertip trails, labels that follow the hands, match cuts solved by fingertip position.
- **Watch:** subtle overlays on normal-looking footage tend not to land; transform the image boldly.

### Tech-showcase effects (datamosh, x-ray, contour sketch)
- **Build:** optical-flow datamosh (`vision/flow` + remap), neon skeletons (`vision/pose`), scan-line contour sketch (`vision/contour`).
- **Watch:** effects without an idea read as forced. Use them only in service of a concept.

### Video-game parody (open-world mission)
- **Build:** loading screen, mission title, a detailed HUD (weapon roundel, bars, money, stars, rotating radar), objectives, popups, a mission marker, an item pickup, cutscene subtitles, a "mission passed" sting (`sfx.fanfare`, original). Use a free lookalike font.
- **Watch:** real game audio carries a copyright/mute risk. Flag it.

### 2.5D parallax
- **Idea:** "most conversations stay on the surface, this one goes deeper".
- **Build:** Core ML depth (`vision/depth`) and `fx/parallax.py` push/orbit/dolly zoom; text at depth planes occluded by nearer people; haze; a flat intro that becomes 3D on the drop.

### Talking object (demo)
- **Build:** MediaPipe face landmarks and blendshapes drive a character (e.g. a book-head), lip-synced to a local TTS voice (Kokoro-82M via mlx-audio).

### Anime restyle
- **Build:** AnimeGAN2 (face_paint_512_v2 / paprika) on face crops plus a cel-shade pass.
- **Watch:** PyTorch MPS leaks memory in long loops; restart the worker every ~40 frames and call `torch.mps.empty_cache()`.

### Music-video parody (2000s rap video)
- **Idea:** a lyric's verb gets struck out in red marker and replaced by your own (e.g. DO → READ).
- **Build:** tan-mapped fisheye remap with push, roll and punch-in; bright warm grade with screen-blend bloom; chrome/gold mixtape type (italic skew, metallic gradient, outline, hard shadow, glint); a music-video credit block lower-left; split screens; a hydraulic "hop" on every beat; flash frames; tape-stop into an end card.
- **Watch:** find lyric timestamps with faster-whisper plus an `initial_prompt` naming the expected line. Keep under 30 s for licensed music.

### Riso zine, hero's journey
- **Idea:** a group meeting told as a story in chapters: strangers → the call → the clash → every voice → the shift → the return.
- **Build:** two-ink risograph print: people in one fluorescent ink through person mattes, the room in another, real rotated dot screens, misregistration, newsprint grain, 15 fps print-stutter; condensed type plus typewriter labels knocked out to paper; quote panels placed off faces using face boxes (`vision/face`); b-roll every 2 beats under long panels.
- **Watch:**
  - equal screen time per person: close-ups one beat each in a single "every voice" run
  - no panel over a face, measured on every frame
  - pick "balanced" wides by matte (several people, nobody filling the frame)

### Observation edit (freeze, circle, read)
- **Idea:** the style of viral "observation" edits, with no references to any show.
- **Build:** velocity ramp easing into a freeze; white flash; snap-zoom with decaying shake; a hand-drawn circle with a leader line onto a real detail (face boxes snap face targets; hand and phone targets measured on a grid sheet); a two-line typed observation placed off faces. One read per person, equal beats. Finale: every face circled at once, a quarter-beat flashback through all the reads, an end card.
- **Watch:**
  - write reads only from visible details, kept kind and playful
  - when someone must be removed, check every used shot on a contact sheet (they show up in other framings)

### Verdict meter (debate / comment bait)
- **Idea:** two sides of a real argument; a live tug-of-war meter slams toward each side as lines land, never settles, and locks at 50/50 on "YOU DECIDE / COMMENT A OR B".
- **Build:** real voices from the footage (translate non-English speech with faster-whisper `task='translate'` to find lines; subtitles must be checked by a speaker of the language); high-key black and white; edge glow in the speaking side's colour; team tags; keyword-coloured subtitles; punch-in plus shake on each slam; reaction cutaways of others while voices continue (cap any speaker at about 3.5 s on screen).
- **Watch:** keep it fair to both sides; avoid identity or agenda angles.

### Pop-up book (pure motion design, Blender, no footage)
- **Idea:** a 3D paper pop-up book; each page turn pops up a scene on the beat; ends on a scarcity CTA ("one seat left") and a comment keyword.
- **Build:** procedural Blender script (EEVEE, headless); hinged pop-ups with BACK-eased rotation keys; page turns as pivots rotating about the spine; per-spread `hide_render` gating (children don't inherit it); bevels on every box; a cyclorama backdrop; motion blur; CC0 HDRI for light only (the camera sees a flat background via Light Path); CC0 paper normal and colour textures.
- **Watch:**
  - for a wide object in 9:16, shoot from the side so it runs into depth
  - boxes scaled to zero height with bevels render as black bars, so hide them instead
  - the CTA must face the camera and fill the frame
  - spot re-render only the affected frame ranges

---

## Ideas not yet built
Video Depth Anything for flicker-free parallax · CoTracker3 to pin type to surfaces · SAM 2 tiny
click-to-track · RIFE speed ramps · LaMa object removal · Demucs stems for drum-exact cuts.
