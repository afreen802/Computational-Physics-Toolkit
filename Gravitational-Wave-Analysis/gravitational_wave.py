import numpy as np
import matplotlib.pyplot as plt

# Time array

t = np.linspace(0, 10, 5000)

# Chirp signal
signal = (0.1 + 0.09*t) * np.sin(
2*np.pi*(2*t + 0.5*t**2)
)

# Plot signal

plt.figure(figsize=(8,5))

plt.plot(t, signal)

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.title(
"Simulated Gravitational Wave Chirp"
)

plt.grid()

plt.savefig(
"wave_signal.png",
dpi=300
)

plt.show()

# Fourier Transform

fft_signal = np.fft.fft(signal)

freq = np.fft.fftfreq(
len(signal),
d=t[1]-t[0]
)

# Frequency Spectrum

plt.figure(figsize=(8,5))

plt.plot(
freq[:len(freq)//2],
np.abs(
fft_signal[:len(freq)//2]
)
)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.title(
"Frequency Spectrum"
)

plt.grid()

plt.savefig(
"frequency_spectrum.png",
dpi=300
)

plt.show()

