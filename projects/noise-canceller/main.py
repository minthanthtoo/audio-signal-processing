import numpy as np
import pyaudio
import scipy.signal as signal
import matplotlib.pyplot as plt

# Parameters
RATE = 44100  # Sample rate
CHUNK = 1024  # Buffer size

# FIR filter coefficients (simple low-pass filter)
nyquist = RATE / 2.0
cutoff = 5000.0  # Hz
normal_cutoff = cutoff / nyquist
b, a = signal.butter(1, normal_cutoff, btype='low', analog=False)

# Create PyAudio instance
p = pyaudio.PyAudio()

# Open stream
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Set up plot for real-time visualization
plt.ion()
fig, ax = plt.subplots()
x = np.linspace(0, RATE / 2, CHUNK // 2)
line, = ax.plot(x, np.random.rand(CHUNK // 2))
ax.set_ylim(0, 255)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude')

while True:
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    
    # Apply FIR filter to the audio data (simple noise cancellation)
    filtered_data = signal.filtfilt(b, a, data)
    
    # FFT of filtered data
    fft_data = np.fft.fft(filtered_data)
    fft_data = np.abs(fft_data[:CHUNK // 2])  # Magnitude
    
    line.set_ydata(fft_data)
    plt.draw()
    plt.pause(0.01)

# Close stream
stream.stop_stream()
stream.close()
p.terminate()
