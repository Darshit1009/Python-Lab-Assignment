import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
def autocorr(x):
    return np.correlate(x, x, mode='full')


def crosscorr(x, y):
    return np.correlate(x, y, mode='full')

fs1, clean = read("finalS.wav")
if clean.ndim == 2:
    clean = clean.mean(axis=1)
    
clean = clean.astype(float)
clean = clean / np.max(np.abs(clean))
noisy = clean + 0.1 * np.random.randn(len(clean))
noisy = noisy / np.max(np.abs(noisy))
periodicSignal = np.sin(2 * np.pi * 440 * np.arange(len(clean)) / fs1)
periodic = clean + 0.3 * periodicSignal
periodic = periodic / np.max(np.abs(periodic))
ac_clean = autocorr(clean)
ac_noisy = autocorr(noisy)
ac_periodic = autocorr(periodic)
cc_clean_noisy = crosscorr(clean, noisy)
cc_clean_periodic = crosscorr(clean, periodic)
plt.figure(figsize=(14, 12))
plt.subplot(3, 2, 1)
plt.plot(ac_clean)
plt.title("Autocorrelation - Clean Audio")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.subplot(3, 2, 2)
plt.plot(ac_noisy)
plt.title("Autocorrelation - Noisy Audio")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.subplot(3, 2, 3)
plt.plot(ac_periodic)
plt.title("Autocorrelation - Periodic Audio")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.subplot(3, 2, 4)
plt.plot(cc_clean_noisy)
plt.title("Cross-correlation: Clean vs Noisy")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.subplot(3, 2, 5)
plt.plot(cc_clean_periodic)
plt.title("Cross-correlation: Clean vs Periodic")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.tight_layout()
plt.savefig("correlation_results.png", dpi=300, bbox_inches='tight')
print("Plot saved as 'correlation_results.png'")
plt.show(block=True)
