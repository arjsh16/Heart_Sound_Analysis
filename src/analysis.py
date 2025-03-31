import math
import cmath
import time

# Pad a signal to the next power of 2 length
def pad_to_power_of_two(signal):
    n = len(signal)
    next_power = 2 ** math.ceil(math.log2(n))
    
    # Convert NumPy array to list if needed
    if not isinstance(signal, list):
        signal = list(signal)
        
    return signal + [0] * (next_power - n)

# Original Discrete Fourier Transform (DFT)
def compute_dft(signal):
    N = len(signal)
    dft_signal = []
    for k in range(N):
        real_part = 0
        imag_part = 0
        for n in range(N):
            angle = -2 * math.pi * k * n / N
            real_part += signal[n] * math.cos(angle)
            imag_part += signal[n] * math.sin(angle)
        dft_signal.append(complex(real_part, imag_part))
    return dft_signal

# Original Inverse Discrete Fourier Transform (IDFT)
def compute_idft(dft_signal):
    N = len(dft_signal)
    idft_signal = []
    for n in range(N):
        real_part = 0
        imag_part = 0
        for k in range(N):
            angle = 2 * math.pi * k * n / N
            real_part += dft_signal[k].real * math.cos(angle) - dft_signal[k].imag * math.sin(angle)
            imag_part += dft_signal[k].real * math.sin(angle) + dft_signal[k].imag * math.cos(angle)
        idft_signal.append(real_part / N)  # Normalize by N
    return idft_signal

# Compute frequency bins
def compute_freqs(N, sample_rate):
    return [i * sample_rate / N for i in range(N)]

# Filter high frequencies (above cutoff)
def filter_signal(dft_signal, freqs, cutoff=400):
    return [
        dft_signal[i] if freqs[i] <= cutoff else 0
        for i in range(len(dft_signal))
    ]

# Recursive FFT Implementation
def compute_fft(signal):
    # Convert to list if not already
    if not isinstance(signal, list):
        signal = list(signal)
        
    N = len(signal)
    
    # Base case
    if N == 1:
        return signal
    
    # Check if length is a power of 2
    if N & (N-1) != 0:
        raise ValueError("Signal length must be a power of 2 for FFT")
    
    # Split into even and odd indices
    even = compute_fft(signal[0::2])
    odd = compute_fft(signal[1::2])
    
    # Combine results
    result = [0] * N
    for k in range(N // 2):
        twiddle = cmath.exp(-2j * math.pi * k / N)
        result[k] = even[k] + twiddle * odd[k]
        result[k + N // 2] = even[k] - twiddle * odd[k]
    
    return result

# Iterative FFT (more efficient)
def iterative_fft(signal):
    # Convert to list if not already
    if not isinstance(signal, list):
        signal = list(signal)
        
    n = len(signal)
    
    # Check if length is a power of 2
    if n & (n-1) != 0:
        raise ValueError("Signal length must be a power of 2 for FFT")
    
    # Convert to complex numbers
    result = [complex(x) for x in signal]
    
    # Bit-reversal permutation
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        
        if i < j:
            result[i], result[j] = result[j], result[i]
    
    # Compute FFT
    step = 2
    while step <= n:
        half_step = step // 2
        angle_step = -2 * math.pi / step
        
        for m in range(0, n, step):
            for k in range(half_step):
                angle = k * angle_step
                twiddle = cmath.exp(angle * 1j)
                
                a = result[m + k]
                b = result[m + k + half_step] * twiddle
                
                result[m + k] = a + b
                result[m + k + half_step] = a - b
        
        step *= 2
    
    return result

# Inverse FFT
def compute_ifft(fft_signal):
    N = len(fft_signal)
    
    # Check if length is a power of 2
    if N & (N-1) != 0:
        raise ValueError("Signal length must be a power of 2 for IFFT")
    
    # Take complex conjugate
    conjugated = [x.conjugate() for x in fft_signal]
    
    # Compute FFT of conjugated values
    result = iterative_fft(conjugated)
    
    # Take conjugate again and normalize
    return [x.conjugate().real / N for x in result]