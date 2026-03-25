import numpy as np
import matplotlib.pyplot as plt

ac = 1.0
fc = 50.0
fs = 1000
bit_duration = 0.1
bits = [1, 0, 1, 1, 0, 0, 1]

# Create time array and stretch bits to match
num_samples = int(fs * len(bits) * bit_duration)
t = np.linspace(0, len(bits) * bit_duration, num_samples, endpoint=False)
message_signal = np.repeat(bits, int(fs * bit_duration))

carrier_signal = ac * np.sin(2 * np.pi * fc * t)
ask_signal = message_signal * carrier_signal

plt.figure(figsize=(10,10), constrained_layout=True)
plt.suptitle(
    f"Name: Gurpreet Singh Sandhu\n"
    f"Roll No.: 2403143\n\n"
    f"ASK Modulation  |  Fc = {fc} Hz  |  Ac = {ac}",
    fontsize=12,
    fontweight='bold'
)

plt.subplot(3,1,1)
plt.plot(t, message_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t, carrier_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t, ask_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()