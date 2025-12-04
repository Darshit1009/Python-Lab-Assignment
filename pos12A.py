import numpy as np
import matplotlib.pyplot as plt

fs = 1000
duration = 1
timeArray = np.linspace(0, duration, fs * duration, endpoint=False)

freq1 = 5
freq2 = 10
signalOne = np.sin(2 * np.pi * freq1 * timeArray)
signalTwo = np.sin(2 * np.pi * freq2 * timeArray)

combinedSignal = signalOne + signalTwo

plt.figure(figsize=(10, 6))
plt.plot(timeArray, combinedSignal, label='combinedSignal')
plt.plot(timeArray, signalOne, '--', label='signalOne')
plt.plot(timeArray, signalTwo, '--', label='signalTwo')
plt.title('Combined Sine Wave Signal')
plt.xlabel('time [s]')
plt.ylabel('amplitude')
plt.legend()
plt.grid(True)
plt.show()