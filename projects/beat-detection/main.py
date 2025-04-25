import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load an audio file
audio_path = 'your-audio-file.wav'  # Replace with your file path
y, sr = librosa.load(audio_path)

# Apply Short-Time Fourier Transform (STFT)
D = librosa.stft(y)

# Convert amplitude to decibels (dB)
DB = librosa.amplitude_to_db(abs(D), ref=np.max)

# Beat detection
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

# Plot the waveform and beats
plt.figure(figsize=(10, 6))

# Plot the waveform
plt.subplot(2, 1, 1)
librosa.display.waveshow(y, sr=sr)
plt.title('Waveform')

# Plot the spectrogram (STFT)
plt.subplot(2, 1, 2)
librosa.display.specshow(DB, sr=sr, x_axis='time', y_axis='log')
plt.title('Spectrogram (STFT) with Beat Locations')
plt.colorbar(format='%+2.0f dB')

# Overlay beat markers
plt.scatter(librosa.frames_to_time(beats), np.zeros_like(beats), color='r', marker='x', label='Beats')
plt.legend()

plt.tight_layout()
plt.show()

print(f"Detected tempo: {tempo} beats per minute")
print(f"Detected beats: {beats}")
