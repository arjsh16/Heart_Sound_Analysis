
import matplotlib.pyplot as plt
import numpy as np

def plot_signals(t, original_signal, dft_signal, filtered_signal, freqs, N):
    """Plot time-domain and frequency-domain signals."""
    plt.figure(figsize=(12,6))

    # Original signal
    plt.subplot(3,1,1)
    plt.plot(t, original_signal, color="blue")
    plt.title("Original Heart Sound Signal (Time Domain)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    # Frequency spectrum
    plt.subplot(3,1,2)
    plt.plot(freqs[:N//2], np.abs(dft_signal[:N//2]), color="red")
    plt.title("DFT Spectrum of Heart Sound")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")

    # Filtered signal
    plt.subplot(3,1,3)
    plt.plot(t, filtered_signal, color="green")
    plt.title("Filtered Heart Sound Signal (Time Domain)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()