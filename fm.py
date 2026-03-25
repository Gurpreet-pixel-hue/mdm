import numpy as np
import matplotlib.pyplot as plt

ac = float(input("Enter Carrier Amplitude: "))
fc = float(input("Enter Carrier Frequency: "))
am = float(input("Enter Message Amplitude: "))
fm = float(input("Enter Message Frequency: "))
m_index = float(input("Enter Modulation Index: "))
t = np.linspace(0,1,1000)

message_signal = am * np.cos(2* np.pi * fm * t)
carrier_signal = ac * np.cos(2*np.pi*fc* t)
fm_signal = ac * np.cos((2*np.pi*fc*t) + m_index * np.sin(2* np.pi * fm * t))

plt.figure(figsize=(10,10), constrained_layout = True)
plt.suptitle(
    f"Name: Gurpreet Singh Sandhu\n"
    f"Roll No.: 2403143\n\n"
    f"Fc = {fc} Hz   |   Ac = {ac}   |   Am = {am}   |   Fm = {fm} Hz   |   m = {m_index}",
    fontsize=12,
    fontweight='bold'
)

plt.subplot(3,1,1)
plt.plot(t,message_signal)
plt.xlabel("Modulating Signal")
plt.ylabel("Amplitude")

plt.subplot(3,1,2)
plt.plot(t,carrier_signal)
plt.xlabel("Carrier Signal")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t,fm_signal)
plt.xlabel("FM Signal")
plt.ylabel("Amplitude")

plt.show()
