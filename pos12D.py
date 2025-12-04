import numpy as np
import matplotlib.pyplot as plt

fs = 1000
duration = 1
timeArray = np.linspace(0, duration, fs * duration, endpoint=False)

freq = 10
originalSignal = np.sin(2 * np.pi * freq * timeArray)
scaledSignal = 3 * originalSignal

plt.figure(figsize=(10, 6))
plt.plot(timeArray, originalSignal, label='originalSignal', color='blue')
plt.plot(timeArray, scaledSignal, label='scaledSignal', color='red', linestyle='--')
plt.title('Original vs Scaled 10Hz Sine Wave')
plt.xlabel('time [s]')
plt.ylabel('amplitude')
plt.legend()
plt.grid(True)
plt.show()