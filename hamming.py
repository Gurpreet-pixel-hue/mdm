import random
print("\nGurpreet Singh Sandhu\n2403143\n")
def calculate_parity(bits, positions):
    parity = 0
    for pos in positions:
        parity ^= bits[pos - 1]
    return parity

data = input("Enter 7 data bits: ")

if len(data) != 7 or any(bit not in '01' for bit in data):
    print("Invalid input!")
    exit()

data = list(map(int, data))

hamming = [0] * 11

j = 0
for i in range(11):
    if i + 1 not in [1, 2, 4, 8]:
        hamming[i] = data[j]
        j += 1

hamming[0] = calculate_parity(hamming, [1,3,5,7,9,11])
hamming[1] = calculate_parity(hamming, [2,3,6,7,10,11])
hamming[3] = calculate_parity(hamming, [4,5,6,7])
hamming[7] = calculate_parity(hamming, [8,9,10,11])

print("Generated Hamming Code:    ", "".join(map(str, hamming)))

# --- Modified Section: Random Error Generation ---
pos = random.randint(1, 11)
print(f"\n--- Transmission Simulation ---")
print(f"Randomly flipped bit at position: {pos}")
hamming[pos - 1] ^= 1
                                                                             

print("Code with Error (Received):", "".join(map(str, hamming)))

p1 = calculate_parity(hamming, [1,3,5,7,9,11])
p2 = calculate_parity(hamming, [2,3,6,7,10,11])
p4 = calculate_parity(hamming, [4,5,6,7])
p8 = calculate_parity(hamming, [8,9,10,11])

error_position = p8*8 + p4*4 + p2*2 + p1*1

print("\n--- Receiver Diagnostics ---")
if error_position == 0:
    print("No error detected")
else:
    print("Detected Error at position:", error_position)
    hamming[error_position - 1] ^= 1
    print("Corrected Code:            ", "".join(map(str, hamming)))
