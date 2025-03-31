# Heart Sound Analysis Using DSP

## Overview
This project analyzes heart sound signals using Fast Fourier Transform (FFT) and Inverse FFT (IFFT) to extract useful frequency components and filter out noise. The implementation follows DSP principles for FFT and IFFT calculations.

## Features
- Load and preprocess heart sound signals  
- Compute FFT to analyze frequency content  
- Filter out high-frequency noise (>400 Hz)  
- Compute IFFT to reconstruct the filtered signal  
- Visualize the original, frequency spectrum, and filtered signals  

## Project Structure
```
Heart_Sound_Analysis/
│── data/
│   ├── heart_sound.wav  # Sample heart sound file
│── src/
│   ├── preprocess.py  # Signal loading & preprocessing
│   ├── analysis.py    # FFT, IFFT & filtering
│   ├── visualization.py  # Plot time & frequency domain signals
│   ├── main.py        # Run the entire pipeline
│── requirements.txt   # Required Python packages
│── README.md          # Project documentation
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/arjsh16/Heart_Sound_Analysis.git
   cd Heart_Sound_Analysis
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the project:
   ```sh
   cd path/to/src
   python main.py
   ```

## How It Works
1. **Preprocessing**
   - Loads the heart sound WAV file.
   - Resamples to 4 kHz, as heart sounds are typically below 400 Hz.
   
2. **FFT Computation** 
   - Converts the signal from time domain to frequency domain.
   
3. **Filtering**
   - Removes high frequencies (>400 Hz) to denoise the signal.
   
4. **IFFT Computation**
   - Reconstructs the time-domain signal from filtered frequency components.
   
5. **Visualization**
   - Plots the original signal, frequency spectrum, and filtered signal.

## Dependencies (`requirements.txt`)
```
matplotlib
librosa
scipy
``` 

## License
MIT License. Feel free to modify and improve!
