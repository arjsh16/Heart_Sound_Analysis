import time
from preprocess import *
from analysis import *
from visualization import *

# Load heart sound
print("------------------------Taking the sample-------------------------")
file_path = "Data/7-adult-heart-sounds-mp3/adultCASE3c.mp3"
signal, sample_rate = load_heart_sound(file_path)
print("------------------------Sample Accquired--------------------------")
print(f"Sample length: {len(signal)}")

# Convert to Python list if needed
if not isinstance(signal, list):
    signal = list(signal)

# Time vector
N = len(signal)
t = [i / sample_rate for i in range(N)]

# Pad signal to power of 2 for FFT
print("--------------------------Padding Signal--------------------------")
padded_signal = pad_to_power_of_two(signal)
padded_N = len(padded_signal)
print(f"Padded to length: {padded_N}")

# Measure time for both implementations
print("--------------------------Timing Analysis-------------------------")

# Time original DFT (on a small subset to make it faster)
subset_size = min(1000, N)
start_time = time.time()
print(f"--------------------------Computing DFT (subset: {subset_size})---------------------------")
dft_signal = compute_dft(signal[:subset_size])
dft_time = time.time() - start_time
print(f"Original DFT time (subset): {dft_time:.4f} seconds")

# Time FFT implementation
start_time = time.time()
print("--------------------------Computing FFT---------------------------")
fft_signal = iterative_fft(padded_signal)
fft_time = time.time() - start_time
print(f"FFT time (full signal): {fft_time:.4f} seconds")
print(f"Estimated full DFT time: {dft_time * (padded_N / subset_size)**2:.4f} seconds")
print(f"Estimated speedup factor: {(dft_time * (padded_N / subset_size)**2) / fft_time:.2f}x")
print("----------------------Computation Complete------------------------")

# Compute frequency bins
freqs = compute_freqs(padded_N, sample_rate)

# Apply filtering
print("---------------------------Filtering now--------------------------")
filtered_fft = filter_signal(fft_signal, freqs)
print("----------------------Completed Filtering-------------------------")

# Convert back to time domain
print("-------------------------Computing IFFT---------------------------")
start_time = time.time()
filtered_signal = compute_ifft(filtered_fft)
ifft_time = time.time() - start_time
print(f"IFFT time: {ifft_time:.4f} seconds")
print("----------------------Computation Complete------------------------")

# Trim to original length
filtered_signal = filtered_signal[:N]

# Convert results back to the format expected by visualization functions
# This tries to maintain compatibility while avoiding NumPy
print("-----------------------------Plotting-----------------------------")
try:
    # Try with the Python lists directly
    plot_signals(t, signal, fft_signal[:padded_N//2], filtered_signal, freqs[:padded_N//2], N)
except Exception as e:
    print(f"Warning: Visualization error: {e}")
    print("Your visualization functions may require NumPy arrays.")
    print("You may need to modify your visualization functions to accept Python lists.")
    print("Alternatively, you can add the following code to convert lists to NumPy arrays:")
    print("    import numpy as np")
    print("    t_np = np.array(t)")
    print("    signal_np = np.array(signal)")
    print("    fft_np = np.array([complex(x.real, x.imag) for x in fft_signal[:padded_N//2]])")
    print("    filtered_np = np.array(filtered_signal)")
    print("    freqs_np = np.array(freqs[:padded_N//2])")
    print("    plot_signals(t_np, signal_np, fft_np, filtered_np, freqs_np, N)")

print("------------------------Process Complete--------------------------")