import numpy as np
import matplotlib.pyplot as plt

ac = 1.0
f0 = 20.0
f1 = 80.0
fs = 1000
bit_duration = 0.1
bits = [1, 0, 1, 1, 0, 0, 1]

num_samples = int(fs * len(bits) * bit_duration)
t = np.linspace(0, len(bits) * bit_duration, num_samples, endpoint=False)
message_signal = np.repeat(bits, int(fs * bit_duration))

# Dynamically swap frequency based on bit value
freq_signal = np.where(message_signal == 1, f1, f0)
fsk_signal = ac * np.sin(2 * np.pi * freq_signal * t)

plt.figure(figsize=(10,10), constrained_layout=True)
plt.suptitle(
    f"Name: Gurpreet Singh Sandhu\n"
    f"Roll No.: 2403143\n\n"
    f"FSK Modulation  |  F0 = {f0} Hz  |  F1 = {f1} Hz",
    fontsize=12,
    fontweight='bold'
)

plt.subplot(2,1,1)
plt.plot(t, message_signal)
plt.xlabel("Time")
plt.ylabel("bit value")
plt.grid(True)

# Note: No single carrier to plot for FSK, so we plot the dynamic frequency array
plt.subplot(2,1,2)
plt.plot(t, fsk_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)



plt.show()