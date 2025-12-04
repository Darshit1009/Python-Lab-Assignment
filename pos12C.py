import numpy as np
import matplotlib.pyplot as plt

fs = 1000
duration = 1
timeArray = np.linspace(0, duration, fs * duration, endpoint=False)

freq = 5
originalSignal = np.sin(2 * np.pi * freq * timeArray)
shiftedSignal = np.sin(2 * np.pi * freq * (timeArray - 0.1))

plt.figure(figsize=(10, 6))
plt.plot(timeArray, originalSignal, label='originalSignal', color='blue')
plt.plot(timeArray, shiftedSignal, label='shiftedSignal', color='red', linestyle='--')
plt.title('Original vs Shifted 5Hz Sine Wave')
plt.xlabel('time [s]')
plt.ylabel('amplitude')
plt.legend()
plt.grid(True)
plt.show()