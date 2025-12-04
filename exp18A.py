import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import AudioFileClip
import scipy as sp
audioClip = AudioFileClip("wave.mp4")
audioClip.write_audiofile("finalS.wav")
sampleRateAudio, audioSignal = sp.io.wavfile.read("finalS.wav")
if audioSignal.ndim == 2:
    audioSignal = audioSignal.mean(axis=1)
audioSignal = audioSignal.astype(np.float32) / np.max(np.abs(audioSignal))
impulseResponse = np.zeros(500, dtype=np.float32)
impulseResponse[0] = 1.0
impulseResponse[100] = 0.6
impulseResponse[300] = 0.3
linearResult = sp.signal.convolve(audioSignal, impulseResponse, mode="full")
signalLength = max(len(audioSignal), len(impulseResponse))
audioPadded = np.pad(audioSignal, (0, signalLength - len(audioSignal)))
impulsePadded = np.pad(impulseResponse, (0, signalLength - len(impulseResponse)))
circularResult = np.fft.ifft(np.fft.fft(audioPadded) * np.fft.fft(impulsePadded)).real
def toInt16(signal):
    signal = signal / np.max(np.abs(signal))
    return (signal * 32767).astype(np.int16)
sp.io.wavfile.write("linearResult.wav", sampleRateAudio, toInt16(linearResult))
sp.io.wavfile.write("circularResult.wav", sampleRateAudio, toInt16(circularResult))
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(audioSignal, color="blue")
plt.title("Original Audio Signal")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.subplot(3, 1, 2)
plt.plot(linearResult, color="green")
plt.title("Linear Convolution Result")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.subplot(3, 1, 3)
plt.plot(circularResult, color="red")
plt.title("Circular Convolution Result")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()
