import numpy as np
import matplotlib.pyplot as plt
ac = float(input("Enter Carrier Amplitude: "))
fc = float(input("Enter Carrier Frequency: "))
am = float(input("Enter Message Amplitude: "))
fm = float(input("Enter Message Frequency: "))
m_index = float(input("Enter Modulation Index: "))

t = np.linspace(0,1,1000)

message_signal = am * np.cos(2*np.pi*fm*t)
carrier_signal = ac * np.cos(2*np.pi*fc*t)
am_signal = ac * (1 + m_index * np.cos(2*np.pi*fm*t)) * np.cos(2*np.pi*fc*t)

plt.figure(figsize=(10,10), constrained_layout = True)
plt.suptitle(
        f"Amplitude Modulation\n"
        f"Name: Gurpreet Singh Sandhu\n"
    f"Roll No.: 2403143\n\n"
    f"Fc = {fc} Hz   |   Ac = {ac}   |   Am = {am}   |   Fm = {fm} Hz   |   m = {m_index}",
    fontsize=12,
    fontweight='bold'
             )

plt.subplot(3,1,1)
plt.plot(t*1000, message_signal, color = 'black', linewidth = 1)
plt.ylabel("Amplitude")
plt.xlabel("Modulating signal")
plt.grid(False)

plt.subplot(3,1,2)
plt.plot(t*1000, carrier_signal, color = 'black', linewidth = 1)
plt.ylabel("Amplitude")
plt.xlabel("Carrier Signal")
plt.grid(False)

plt.subplot(3,1,3)
plt.plot(t*1000, am_signal, color = 'black', linewidth = 1)
plt.ylabel("Amplitude")
plt.xlabel("Modulated Signal")
plt.grid(False)
plt.show()

