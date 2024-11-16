#Write a function that takes two equal-length buffers and produces their XOR combination.

def xor_buffers(buffer1: bytes, buffer2: bytes) -> bytes:
    if len(buffer1) != len(buffer2):
        raise ValueError("Buffers must be of equal length")
    return bytes(a ^ b for a, b in zip(buffer1, buffer2))

# Example usage with hexadecimal strings
buffer1 = bytes.fromhex("1c0111001f010100061a024b53535009181c") #input1
buffer2 = bytes.fromhex("686974207468652062756c6c277320657965") #input2

try:
    result = xor_buffers(buffer1, buffer2)
    print("XOR result:", result.hex())
    
except ValueError as e:
    print("Error:", e)
