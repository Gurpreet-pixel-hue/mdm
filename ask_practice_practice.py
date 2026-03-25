import numpy as np
import matplotlib.pyplot as plt

ac = 1.0
fc = 50.0
fs = 1000
bit_duration = 0.1
bits = [1,0,1,1,0,0,1]

num_samples = int(fs * len(bits) * bit_duration)
t = np.linspace(0, len(bits)*bit_duration, num_samples,endpoint=False)
message_signal = np.repeat(bits, int(fs * bit_duration))