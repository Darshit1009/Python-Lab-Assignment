import numpy as np
import matplotlib.pyplot as plt

fs = 500
duration = 2
timeArray = np.linspace(0, duration, fs * duration, endpoint=False)

freqSine = 5
freqCosine = 10
sineSignal = np.sin(2 * np.pi * freqSine * timeArray)
cosineSignal = np.cos(2 * np.pi * freqCosine * timeArray)

productSignal = sineSignal * cosineSignal

plt.figure(figsize=(10, 6))
plt.plot(timeArray, productSignal, label='productSignal', color='blue')
plt.title('Product of 5Hz Sine and 10Hz Cosine')
plt.xlabel('time [s]')
plt.ylabel('amplitude')
plt.legend()
plt.grid(True)
plt.show()