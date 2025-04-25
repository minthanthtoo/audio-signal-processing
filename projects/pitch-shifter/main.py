import numpy as np
import pyaudio
import librosa
import soundfile as sf

# Parameters
RATE = 44100  # Sample rate
CHUNK = 1024  # Buffer size

# Load an audio file
y, sr = librosa.load('your-audio-file.wav', sr=RATE)

# Shift pitch (by factor of 1.5 for example)
y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=4)  # 4 steps up in pitch

# Save the pitch-shifted audio
sf.write('pitch-shifted-audio.wav', y_shifted, RATE)

# Play the pitch-shifted audio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                output=True)

# Stream audio data
stream.write(y_shifted.astype(np.int16).tobytes())
stream.stop_stream()
stream.close()
p.terminate()
