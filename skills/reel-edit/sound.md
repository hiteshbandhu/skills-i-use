# Sound: music, beat grid, SFX, mix

## Music

- **Mixkit** (mixkit.co/free-stock-music): free licence, social use OK, no attribution needed. Direct file URLs follow `https://assets.mixkit.co/music/<id>/<id>.mp3`. Ask the user before downloading.
- Pixabay blocks automated downloads with a bot check, so let the user fetch from there.
- Tracks that worked: Tech House vibes (collage, poster), Midnight Funk (behind-words), Just Keep Walking (glyph), #431 92 BPM G-funk (GTA), #282 (parallax), Driving Ambition (trailer).
- Match energy to concept: graphic/collage → tech house or funk; cinematic → a build with clear hits; game parody → the genre's sound, with original stings.
- Game/film audio (e.g. a famous quote) carries a mute/copyright risk. Use it only with consent and flag it at delivery.

## Beat grid

`beats.py track.mp3` prints tempo, energy per second, kick energy per second and the strongest low-end onsets (drop candidates). Choose `--start` so that:
- the reel opens 2–8 beats before a drop (tension, then release on a visible event);
- the loudest section covers the middle of the reel;
- the ending lands on a phrase boundary, or fade out over 1.2–1.6 s.

Then cut on `grid[i]`, slam type on kicks, and put small motion on off-beats. librosa's beat tracker can be half or double time; check `60/tempo` against the grid spacing.

## SFX (scripts/sfx.py)

Synthesised, so there's no licensing: `riser swell whoosh thump braam tick tok paper shutter pad fanfare` plus `tape_stop()` and `reverb()`. Audition them with `python3 scripts/sfx.py demo demo.wav`.

| Event | Sound | Level vs music |
|---|---|---|
| into a drop | `riser` 1.5–2.2 s ending on the hit | -12 to -14 dB |
| hard cut / title slam | `thump` (+ `braam` for trailers) | -6 to -10 dB |
| card / stamp / sticker lands | `tok` or `paper` | -12 dB |
| strobe card | `tick` | -14 dB |
| photo / flash-freeze | `shutter` | -10 dB |
| "mission passed" / end sting | `fanfare` | -8 dB |
| power-off ending | `tape_stop(mix_tail)` | n/a |

Only put SFX on things the viewer sees happen. Cartoon boings and stock whoosh packs cheapen it.

## Mix (scripts/mix.py)

- Natural sound from the clips sits at -16 to -25 dB under the music. Every clip edge gets a 40 ms fade.
- Speech-led: duck the music by -8 to -12 dB under speech (`duck` ranges have 120 ms ramps).
- Clone or multi-voice gags: pan each voice to its on-screen side (`pan` -1..1).
- A hard silence before a title (`silence`) hits harder than any SFX.
- Master: measure integrated loudness, apply a static gain to -14 LUFS, then `alimiter` at 0.89. Don't use `loudnorm` on dynamic mixes.
