"""Procedural horror soundtrack: writes audio/<name>.ogg (needs numpy + ffmpeg).

Every looping track is built on a circular timeline (events wrap around and the
reverb is a circular FFT convolution), so the loops are seamless.

Tracks
  title    music-box lullaby over a soft drone
  upper    dungeon ambience: low drone, water drips, distant metal
  deep     heartbeat, lower drone, wet rumble
  abyss    dissonant cluster drone, whispers
  gate     tense low pulse for gatekeepers
  lullaby  the wordless lullaby, hummed (overlay for lullaby scenes)
  ending   warm lullaby in the major mode
  gameover low bell + fading drone (one shot)
"""
import os, subprocess, wave
import numpy as np

SR = 22050
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'audio')
rng = np.random.default_rng(7)


def note_hz(n):
    """MIDI note number -> Hz."""
    return 440.0 * 2 ** ((n - 69) / 12)


def place(buf, sig, start):
    """Add sig into circular buffer at sample index start (wraps around)."""
    n = len(buf)
    idx = (np.arange(len(sig)) + int(start)) % n
    np.add.at(buf, idx, sig)


def env(n, a=0.005, d=1.0, sr=SR):
    t = np.arange(n) / sr
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)
    return e


def music_box(f, dur=2.5):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t * 3)
         + 0.15 * np.sin(2 * np.pi * 4.07 * f * t) * np.exp(-t * 6))
    return s * env(n, 0.003, 0.9)


def hum(f, dur):
    """Wordless humming voice: harmonics shaped like a closed-mouth 'mm', with vibrato."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    vib = 1 + 0.006 * np.sin(2 * np.pi * 5.2 * t) * np.minimum(1, t / 0.4)
    ph = 2 * np.pi * np.cumsum(f * vib) / SR
    s = np.zeros(n)
    for k, a in ((1, 1.0), (2, 0.55), (3, 0.25), (4, 0.12), (5, 0.06)):
        s += a * np.sin(k * ph)
    a_ = np.minimum(1, t / 0.09)
    r_ = np.minimum(1, (dur - t) / 0.18)
    return s * a_ * np.clip(r_, 0, 1) * 0.5


def drone(n, notes, amp=0.2, lfo=0.05, detune=0.3):
    t = np.arange(n) / SR
    L = n / SR
    s = np.zeros(n)
    for i, m in enumerate(notes):
        f = note_hz(m)
        for d in (-detune, 0, detune):
            # snap frequency to an integer number of cycles per loop -> seamless
            ff = round((f + d) * L) / L
            s += np.sin(2 * np.pi * ff * t + i)
    l = round(lfo * L) / L if lfo else 0
    s *= 0.6 + 0.4 * np.sin(2 * np.pi * l * t) if l else 1
    return s / (len(notes) * 3) * amp


def filtered_noise(n, lo, hi, amp):
    spec = np.fft.rfft(rng.standard_normal(n))
    fr = np.fft.rfftfreq(n, 1 / SR)
    spec *= ((fr > lo) & (fr < hi)).astype(float)
    s = np.fft.irfft(spec, n)
    return s / (np.abs(s).max() + 1e-9) * amp


def reverb(sig, seconds=2.5, mix=0.35):
    """Circular convolution with a decaying-noise impulse response (keeps loops seamless)."""
    n = len(sig)
    m = min(n, int(seconds * SR))
    ir = rng.standard_normal(m) * np.exp(-np.arange(m) / (SR * seconds / 5))
    ir = np.concatenate([ir, np.zeros(n - m)])
    wet = np.fft.irfft(np.fft.rfft(sig) * np.fft.rfft(ir), n)
    wet /= (np.abs(wet).max() + 1e-9)
    return sig * (1 - mix) + wet * mix * (np.abs(sig).max() + 1e-9)


def drip():
    n = int(0.12 * SR)
    t = np.arange(n) / SR
    f = 1400 * np.exp(-t * 9) + 500
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 35) * 0.5


def clang(f=210):
    n = int(3.0 * SR)
    t = np.arange(n) / SR
    s = sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t * (1.2 + r * 0.4)) for r, a in ((1, 1), (2.76, .5), (5.4, .3), (8.9, .15)))
    return s * 0.25


def thump(f=55):
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    ff = f * (1 + 0.6 * np.exp(-t * 30))
    return np.sin(2 * np.pi * np.cumsum(ff) / SR) * np.exp(-t * 11)


# The lullaby (original): A minor, 3/4. (midi note, beats)
MELODY = [(76, 1), (72, 1), (69, 1), (71, 1), (67, 1), (64, 1), (69, 1), (72, 1), (71, 1), (69, 3),
          (76, 1), (72, 1), (69, 1), (71, 1), (67, 1), (64, 1), (65, 1), (69, 1), (68, 1), (69, 3)]
CHORDS = [[45, 52, 57], [40, 47, 52], [45, 52, 57], [45, 52, 57], [45, 52, 57], [40, 47, 52], [38, 45, 50], [45, 52, 57]]


def lullaby(voice, beat=0.62, transpose=0, major=False, chords=True, amp=0.5):
    bars = 8
    n = int(bars * 3 * beat * SR)
    buf = np.zeros(n)
    t0 = 0.0
    for m, b in MELODY:
        if major and m % 12 in (0, 4, 5):     # C->C#, E stays, F->F# : lift to A major colour
            m = m + (1 if m % 12 in (0, 5) else 0)
        f = note_hz(m + transpose)
        sig = music_box(f) if voice == 'box' else hum(f, b * beat * 1.02)
        place(buf, sig * amp, t0 * SR)
        t0 += b * beat
    if chords:
        for i, ch in enumerate(CHORDS):
            for k, m in enumerate(ch):
                if major and m % 12 == 0:
                    m += 1
                place(buf, music_box(note_hz(m + transpose), 3.0) * 0.12, (i * 3 * beat + k * 0.04) * SR)
    return buf


def norm(s, peak=0.8):
    return s / (np.abs(s).max() + 1e-9) * peak


def save(name, s):
    os.makedirs(OUT, exist_ok=True)
    wav = os.path.join(OUT, name + '.wav')
    data = (np.clip(s, -1, 1) * 32000).astype('<i2')
    with wave.open(wav, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(data.tobytes())
    ogg = os.path.join(OUT, name + '.ogg')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav, '-c:a', 'libvorbis', '-q:a', '2', ogg], check=True)
    os.remove(wav)
    print(name, '%.1fs' % (len(s) / SR), '%d KB' % (os.path.getsize(ogg) // 1024))


def track_title():
    lb = lullaby('box', beat=0.68)
    n = len(lb) * 2
    s = np.concatenate([lb, lullaby('box', beat=0.68, transpose=-12, amp=0.35)])
    s += drone(n, [45, 52], 0.10, lfo=0.04)
    s += filtered_noise(n, 200, 900, 0.015)
    return norm(reverb(s, 3.0, 0.45), 0.7)


def track_upper():
    n = int(40 * SR)
    s = drone(n, [33, 40, 45], 0.35, lfo=0.05)
    s += filtered_noise(n, 80, 400, 0.06)            # wind
    for _ in range(26):
        place(s, drip() * rng.uniform(0.2, 0.6), rng.integers(0, n))
    for k in range(2):
        place(s, clang(rng.uniform(170, 260)) * 0.5, rng.integers(0, n))
    return norm(reverb(s, 3.5, 0.5), 0.7)


def track_deep():
    n = int(40 * SR)
    s = drone(n, [28, 35, 40], 0.35, lfo=0.08)
    s += filtered_noise(n, 40, 220, 0.10)
    beat = 60 / 54
    t = 0.0
    while t < n / SR:
        place(s, thump(52) * 0.9, t * SR)
        place(s, thump(46) * 0.6, (t + 0.28) * SR)
        t += beat
    for _ in range(10):
        place(s, drip() * 0.25, rng.integers(0, n))
    return norm(reverb(s, 2.5, 0.35), 0.75)


def track_abyss():
    n = int(40 * SR)
    s = drone(n, [33, 34, 40, 46], 0.4, lfo=0.03, detune=0.6)   # minor-second cluster
    s += filtered_noise(n, 60, 180, 0.08)
    for _ in range(14):                                          # whispers
        m = int(rng.uniform(0.4, 1.2) * SR)
        w = filtered_noise(m, 1500, 4500, 0.12) * np.sin(np.linspace(0, np.pi, m)) ** 2
        place(s, w, rng.integers(0, n))
    place(s, hum(note_hz(64), 3.0) * 0.12, int(n * 0.6))         # a distant fragment of the lullaby
    place(s, hum(note_hz(60), 3.0) * 0.10, int(n * 0.6 + 3.1 * SR))
    return norm(reverb(s, 4.0, 0.55), 0.7)


def track_gate():
    n = int(24 * SR)
    s = drone(n, [29, 36, 41], 0.3, lfo=0.25)
    t = 0.0
    while t < n / SR:
        place(s, thump(42) * 0.8, t * SR)
        place(s, thump(42) * 0.5, (t + 0.5) * SR)
        t += 1.5
    s += filtered_noise(n, 100, 600, 0.05) * (0.5 + 0.5 * np.sin(2 * np.pi * np.arange(n) / n))
    for _ in range(3):
        place(s, clang(rng.uniform(120, 160)) * 0.4, rng.integers(0, n))
    return norm(reverb(s, 2.0, 0.3), 0.8)


def track_lullaby():
    s = lullaby('hum', beat=0.7, chords=False, amp=0.6)
    s += drone(len(s), [45], 0.05, lfo=0)
    return norm(reverb(s, 3.5, 0.55), 0.6)


def track_ending():
    a = lullaby('box', beat=0.72, transpose=0, major=True)
    b = lullaby('hum', beat=0.72, major=True, chords=False, amp=0.35)
    s = a + b
    s += drone(len(s), [45, 52, 57], 0.08, lfo=0.02)
    return norm(reverb(s, 3.0, 0.4), 0.7)


def track_gameover():
    n = int(6 * SR)
    s = np.zeros(n)
    place(s, clang(98) * 1.2, 0)
    t = np.arange(n) / SR
    s += drone(n, [28, 35], 0.25, lfo=0) * np.exp(-t / 2.5)
    s = norm(reverb(s, 3.0, 0.4), 0.8)
    s[-int(1.0 * SR):] *= np.linspace(1, 0, int(1.0 * SR))
    return s


def sfx_steps():
    """Footsteps going down stone stairs: four steps, each a bit further and quieter."""
    n = int(2.4 * SR)
    s = np.zeros(n)
    for i in range(4):
        m = int(0.16 * SR)
        t = np.arange(m) / SR
        scuff = filtered_noise(m, 90, 1400 - i * 200, 0.6) * np.exp(-t * 38)
        knock = np.sin(2 * np.pi * (78 - i * 4) * t) * np.exp(-t * 26) * 0.9
        place(s, (scuff + knock) * (0.95 - i * 0.18), (0.05 + i * 0.36 + (0.03 if i % 2 else 0)) * SR)
    s = norm(reverb(s, 1.4, 0.32), 0.85)
    s[-int(0.4 * SR):] *= np.linspace(1, 0, int(0.4 * SR))
    return s


if __name__ == '__main__':
    save('sfx_steps', sfx_steps())
    for name, fn in (('title', track_title), ('upper', track_upper), ('deep', track_deep), ('abyss', track_abyss),
                     ('gate', track_gate), ('lullaby', track_lullaby), ('ending', track_ending), ('gameover', track_gameover)):
        save(name, fn())
