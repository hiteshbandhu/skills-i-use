#!/usr/bin/env python3
"""Word-level transcript with faster-whisper, fully offline after the first download.

  transcribe.py <media> [--model small.en|medium|medium.en] [--lang en] [--out words.json] [--srt out.srt]
Lessons: set HF_HUB_OFFLINE=1 once the model is cached (it otherwise hangs on a
network check); temperature=0 + condition_on_previous_text=False avoids the slow
fallback loop; only transcribe clips that actually contain speech (check
mean_db in manifest.json). Hinglish/noisy café audio is not worth transcribing.
"""
import argparse, json, os

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('media'); ap.add_argument('--model', default='small.en'); ap.add_argument('--lang')
    ap.add_argument('--out'); ap.add_argument('--srt')
    a = ap.parse_args()
    from huggingface_hub import try_to_load_from_cache
    if try_to_load_from_cache(f'Systran/faster-whisper-{a.model}', 'model.bin'):
        os.environ['HF_HUB_OFFLINE'] = '1'
    from faster_whisper import WhisperModel
    m = WhisperModel(a.model, device='cpu', compute_type='int8')
    # decode with ffmpeg ourselves: faster-whisper's PyAV path breaks on some Python/av versions
    import subprocess, numpy as np
    pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', a.media, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'],
                         capture_output=True, check=True).stdout
    audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
    segs, info = m.transcribe(audio, language=a.lang, word_timestamps=True, temperature=0,
                              condition_on_previous_text=False, vad_filter=True)
    words, srt = [], []
    for i, s in enumerate(segs, 1):
        for w in s.words or []:
            words.append(dict(w=w.word.strip(), s=round(w.start, 3), e=round(w.end, 3), p=round(w.probability, 2)))
        ts = lambda x: f'{int(x//3600):02d}:{int(x%3600//60):02d}:{int(x%60):02d},{int(x*1000%1000):03d}'
        srt.append(f'{i}\n{ts(s.start)} --> {ts(s.end)}\n{s.text.strip()}\n')
        print(f'[{s.start:7.2f} - {s.end:7.2f}] {s.text.strip()}')
    out = a.out or os.path.splitext(a.media)[0] + '.words.json'
    json.dump(dict(language=info.language, words=words), open(out, 'w'), indent=0)
    if a.srt: open(a.srt, 'w').write('\n'.join(srt))
    print('words ->', out)

if __name__ == '__main__':
    main()
