import numpy as np
import matplotlib.pyplot as plt

ac = float(input("Enter Carrier Amplitude: "))
fc = float(input("Enter Carrier Frequency: "))
am = float(input("Enter Message Amplitude: "))
fm = float(input("Enter Message Frequency: "))
m_index = float(input("Enter Modulation Index: "))

t = np.linspace(0,1,1000)

message_signal = am * np.cos(2*np.pi*fm* t)
carrier_signal = ac * np.cos(2*np.pi*fc*t)
am_signal = ac * (1 + m_index*np.cos(2*np.pi*fm*t)) * np.cos(2*np.pi*fc*t)

plt.figure(figsize=(10,10), constrained_layout = True)
plt.suptitle(f"AC: {ac}")
plt.subplot(3,1,1)
plt.plot(t,message_signal)

plt.subplot(3,1,2)
plt.plot(t,carrier_signal)

plt.subplot(3,1,3)
plt.plot(t,am_signal)

plt.show()