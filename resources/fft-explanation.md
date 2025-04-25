# FFT Explanation

## Overview

The **Fast Fourier Transform (FFT)** is an algorithm to compute the **Discrete Fourier Transform (DFT)** and its inverse. The Fourier Transform is a mathematical technique used to transform a signal from its original domain (often time or space) into the frequency domain. In the frequency domain, a signal is represented by its frequency components.

The FFT is widely used in many applications such as audio processing, communications, image processing, and scientific computing because it allows for efficient computation of the DFT.

## Discrete Fourier Transform (DFT)

The **Discrete Fourier Transform (DFT)** is defined by the following equation:

\[
X(k) = \sum_{n=0}^{N-1} x(n) e^{-j 2 \pi k n / N}
\]

Where:
- \( X(k) \) is the frequency component at index \( k \),
- \( x(n) \) is the signal at time index \( n \),
- \( N \) is the total number of samples in the signal,
- \( e^{-j 2 \pi k n / N} \) represents the complex sinusoidal basis functions.

### Key Concepts:
- **Time domain**: The original signal, where you have amplitude over time.
- **Frequency domain**: The transformed signal, where you have frequency components (amplitude and phase) over frequency.

## Fast Fourier Transform (FFT)

The **FFT** is an optimized version of the DFT that drastically reduces computation time. For a signal with \( N \) samples, computing the DFT directly requires \( O(N^2) \) operations. The FFT reduces this to \( O(N \log N) \), making it much faster and more practical for large datasets.

### FFT Algorithm:
The FFT algorithm works by recursively dividing the DFT into smaller DFTs and exploiting symmetries in the complex roots of unity. A commonly used FFT algorithm is the **Cooley-Tukey algorithm**, which recursively divides the DFT into even and odd parts.

## Applications of FFT

- **Audio Signal Processing**: FFT is used to analyze the frequency content of audio signals. It allows us to determine pitch, detect musical notes, and visualize sound as spectrograms.
- **Communication Systems**: In digital communication, FFT is used in modulation and demodulation, such as in **OFDM (Orthogonal Frequency Division Multiplexing)**.
- **Radar and Sonar**: FFT is used to analyze the frequency shifts in radar and sonar signals, such as for detecting target velocity (Doppler effect).
- **Image Processing**: In images, FFT is used to detect patterns, enhance image features, or remove noise.

## Understanding FFT Results

When you apply FFT to a signal, you get the **frequency spectrum** of that signal. The result of an FFT contains both **amplitude** and **phase** information.

### Frequency Spectrum:

- **Amplitude Spectrum**: Shows how much of each frequency component exists in the signal.
- **Phase Spectrum**: Shows the phase shift of each frequency component.

In practice, the **amplitude spectrum** is often plotted to understand the dominant frequencies in the signal.

## Example: Audio Signal Visualization

Imagine you have a sine wave with a frequency of 5 Hz. When you apply FFT to this sine wave, the result should show a spike at 5 Hz in the frequency domain. If the signal is more complex, with multiple sine waves at different frequencies, the FFT will show multiple peaks at those frequencies.

## Code Example: Using FFT in Python

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate a sample signal: a combination of two sine waves (5 Hz and 50 Hz)
sampling_rate = 1000  # Samples per second
duration = 1  # seconds
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)

# Apply FFT
n = len(signal)
frequencies = np.fft.fftfreq(n, 1/sampling_rate)
fft_values = np.fft.fft(signal)

# Compute amplitude spectrum
amplitude = np.abs(fft_values)

# Plot the results
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(frequencies[:n // 2], amplitude[:n // 2])  # Only plot positive frequencies
plt.title('Amplitude Spectrum (FFT)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
