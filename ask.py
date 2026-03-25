#  ASK - Amplitude Shift Keying  (Practical Demo)
#  pip install numpy matplotlib
# ============================================================
import numpy as np
import matplotlib.pyplot as plt
 
# ---------- 1. Parameters ----------
fs           = 1000   # Sampling frequency (Hz) - samples per second
fc           = 50     # Carrier frequency (Hz)  - sine wave speed
bit_duration = 0.1    # Duration of each bit (seconds)
bits         = [1, 0, 1, 1, 0, 0, 1]   # Digital message to send
 
# ---------- 2. Time axis ----------
num_samples = int(fs * len(bits) * bit_duration)
t = np.linspace(0, len(bits) * bit_duration, num_samples, endpoint=False)
 
# ---------- 3. Carrier signal ----------
carrier = np.sin(2 * np.pi * fc * t)   # A(t) = sin(2*pi*fc*t)
 
# ---------- 4. ASK Modulation ----------
# Stretch each bit value to fill its time slot
message_signal = np.repeat(bits, int(fs * bit_duration))
 
# Multiply bit (0 or 1) by carrier => ON/OFF keying
ask_signal = message_signal * carrier
 
# ---------- 5. Plot results ----------
fig, axes = plt.subplots(3, 1, figsize=(12, 7), sharex=True)
fig.suptitle('ASK - Amplitude Shift Keying', fontsize=14, fontweight='bold')
 
axes[0].plot(t, message_signal, color='steelblue', linewidth=2)
axes[0].set_title('Digital Message (bit stream)')
axes[0].set_ylabel('Bit Value')
axes[0].set_yticks([0, 1])
 
axes[1].plot(t, carrier, color='darkorange', linewidth=1)
axes[1].set_title('Carrier Signal  sin(2pi*fc*t)')
axes[1].set_ylabel('Amplitude')
 
axes[2].plot(t, ask_signal, color='seagreen', linewidth=1)
axes[2].set_title('ASK Modulated Signal')
axes[2].set_ylabel('Amplitude')
axes[2].set_xlabel('Time (seconds)')
 
plt.tight_layout()
plt.show()