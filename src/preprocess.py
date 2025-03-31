
import librosa

def load_heart_sound(file_path, sample_rate=4000):
    """Load heart sound and resample it to the desired sample rate."""
    signal, sr = librosa.load(file_path, sr=sample_rate)
    return signal, sr
