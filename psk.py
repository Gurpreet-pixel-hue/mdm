#  PSK - Phase Shift Keying / BPSK  (Practical Demo)
# ============================================================
import numpy as np
import matplotlib.pyplot as plt
 
# ---------- 1. Parameters ----------
fs           = 1000   # Sampling frequency (Hz)
fc           = 50     # Carrier frequency (Hz)
bit_duration = 0.1    # Duration of each bit (seconds)
bits         = [1, 0, 1, 1, 0, 0, 1]   # Digital message
 
# ---------- 2. PSK (BPSK) Modulation ----------
psk_signal = []
 
for bit in bits:
    t_bit = np.linspace(0, bit_duration,
                        int(fs * bit_duration), endpoint=False)
    # Bit '1' => phase 0 deg  |  Bit '0' => phase 180 deg (pi radians)
    phase = 0 if bit == 1 else np.pi
    segment = np.sin(2 * np.pi * fc * t_bit + phase)
    psk_signal.extend(segment)
 
psk_signal = np.array(psk_signal)
 
# ---------- 3. Time axis ----------
num_samples    = int(fs * len(bits) * bit_duration)
t              = np.linspace(0, len(bits)*bit_duration, num_samples, endpoint=False)
message_signal = np.repeat(bits, int(fs * bit_duration))
 
# ---------- 4. Plot results ----------
fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
fig.suptitle('PSK - Phase Shift Keying (BPSK)', fontsize=14, fontweight='bold')
 
axes[0].step(t, message_signal, color='steelblue', linewidth=2, where='post')
axes[0].set_title('Digital Message (bit stream)')
axes[0].set_ylabel('Bit Value')
axes[0].set_yticks([0, 1])
 
axes[1].plot(t, psk_signal, color='crimson', linewidth=1)
axes[1].set_title('PSK Modulated Signal  (0 deg = bit 1,  180 deg = bit 0)')
axes[1].set_ylabel('Amplitude')
axes[1].set_xlabel('Time (seconds)')
 
plt.tight_layout()
plt.show()