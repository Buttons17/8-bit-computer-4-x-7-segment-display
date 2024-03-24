# length = 2048 # uncomment for 28c16
length = 8192 # uncomment for 28c64
# length = 32768 # uncomment for 28c256

output = bytearray([0xFF] * length)

# common cathode 8 segment display dP, a,b,c,d,e,f,g
digits = [0x7E, 0x30, 0x6D, 0x79, 0x33, 0x5B, 0x5F, 0x70, 0x7F, 0x7B]

# Program the 1s place
for value in range(256):
    output[value] = digits[value % 10]

# Program the 10s place
for value in range(256):
    output[value + 256] = digits[(value // 10) % 10]

# Program the 100s place
for value in range(256):
    output[value + 512] = digits[(value // 100) % 10]

# Program the sign place
for value in range(256):
    output[value + 768] = 0x00

# Program 1s place (twos complement)
for value in range(-128, 128):
    offset = value + 1024 if value >= 0 else value + 1024 + 256
    output[offset] = digits[abs(value) % 10]

# Program 10s place (twos complement)
for value in range(-128, 128):
    offset = value + 1280 if value >= 0 else value + 1280 + 256
    output[offset] = digits[abs(value) // 10 % 10]

# Program 100s place (twos complement)
for value in range(-128, 128):
    offset = value + 1536 if value >= 0 else value + 1536 + 256
    output[offset] = digits[abs(value) // 100 % 10]

# Program sign place (twos complement)
for value in range(-128, 128):
    offset = value + 1792 if value >= 0 else value + 1792 + 256
    output[offset] = 0x01 if value < 0 else 0x00

# Write the output to a binary file
with open("output.bin", "wb") as out_file:
    out_file.write(output)