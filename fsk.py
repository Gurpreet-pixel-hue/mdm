# ============================================================
#  FSK - Frequency Shift Keying  (Practical Demo)
# ============================================================
import numpy as np
import matplotlib.pyplot as plt
 
# ---------- 1. Parameters ----------
fs           = 1000   # Sampling frequency (Hz)
f0           = 20     # Frequency for bit '0' - LOW frequency
f1           = 80     # Frequency for bit '1' - HIGH frequency
bit_duration = 0.1    # Duration of each bit (seconds)
bits         = [1, 0, 1, 1, 0, 0, 1]   # Digital message
 
# ---------- 2. FSK Modulation ----------
fsk_signal = []
 
for bit in bits:
    # Independent time array for each bit segment
    t_bit = np.linspace(0, bit_duration,
                        int(fs * bit_duration), endpoint=False)
    # Choose frequency based on bit value
    freq = f1 if bit == 1 else f0
    segment = np.sin(2 * np.pi * freq * t_bit)
    fsk_signal.extend(segment)         # append segment to signal
 
fsk_signal = np.array(fsk_signal)
 
# ---------- 3. Time axis for full signal ----------
num_samples    = int(fs * len(bits) * bit_duration)
t              = np.linspace(0, len(bits)*bit_duration, num_samples, endpoint=False)
message_signal = np.repeat(bits, int(fs * bit_duration))
 
# ---------- 4. Plot results ----------
fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
fig.suptitle('FSK - Frequency Shift Keying', fontsize=14, fontweight='bold')
 
axes[0].step(t, message_signal, color='steelblue', linewidth=2, where='post')
axes[0].set_title('Digital Message (bit stream)')
axes[0].set_ylabel('Bit Value')
axes[0].set_yticks([0, 1])
 
axes[1].plot(t, fsk_signal, color='purple', linewidth=1)
axes[1].set_title(f'FSK Modulated Signal  (f0={f0} Hz for 0,  f1={f1} Hz for 1)')
axes[1].set_ylabel('Amplitude')
axes[1].set_xlabel('Time (seconds)')
 
plt.tight_layout()
plt.show()