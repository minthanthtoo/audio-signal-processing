import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load an audio file
audio_path = 'your-audio-file.wav'  # Replace with your file path
y, sr = librosa.load(audio_path)

# Apply Short-Time Fourier Transform (STFT)
D = librosa.stft(y)

# Convert amplitude to decibels (dB)
DB = librosa.amplitude_to_db(abs(D), ref=np.max)

# Plot the STFT (Spectrogram)
plt.figure(figsize=(10, 6))
librosa.display.specshow(DB, sr=sr, x_axis='time', y_axis='log')
plt.title('Spectrogram (STFT) of Audio')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
plt.show()
