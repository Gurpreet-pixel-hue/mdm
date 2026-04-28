import numpy as np
import matplotlib.pyplot as plt

ac = float(input("Enter Carrier Amplitude: "))
fc = float(input("Enter Carrier Frequency: "))
am = float(input("Enter Message Amplitude: "))
fm = float(input("Enter Message Freuquency: "))
m = float(input("Enter Modulation Index: "))

t = np.linspace(0,1,1000)
message_signal = am * np.cos(2 * np.pi * fm * t)
carrier_signal = ac * np.cos( 2 * np.pi * fc * t)

fm_signal = ac * np.cos((2*np.pi*fc * t) + m * np.sin(2*np.pi*fm*t))


plt.figure(figsize=(10,10), constrained_layout = True)

plt.subplot(3,1,1)
plt.plot(t,message_signal)
plt.subplot(3,1,2)
plt.plot(t,carrier_signal)
plt.subplot(3,1,3)
plt.plot(t,fm_signal)
plt.show()