# import sys;sys.stdout.buffer.write(b"\x32\x0a" + (b"\x41" * 32) + b"\xa9\x51\x4c\x8a\x6b\x55\x0a\x34\x0a")
# 004011a0

from random import randint

def generator(g, x, p):
    return pow(g, x) % p

def decrypt(ciphertext, key):
    plaintext = []
    for num in ciphertext:
        if num == 0:  # Handle zero values specially
            plaintext.append(' ')
        else:
            # Use integer division and ensure we're getting valid ASCII
            char_code = round(num / (key * 311))
            plaintext.append(chr(char_code))
    return ''.join(plaintext)

def dynamic_xor_decrypt(ciphertext, text_key):
    plain_text = ""
    key_length = len(text_key)
    # Process the string normally (not reversed)
    for i, char in enumerate(ciphertext):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plain_text += decrypted_char
    return plain_text

def decrypt_message():
    # Known values from the encryption
    p = 97
    g = 31
    a = 94
    b = 29
    text_key = "trudeau"
    
    # Encrypted message
    cipher = [260307, 491691, 491691, 2487378, 2516301, 0, 1966764, 1879995, 1995687, 
              1214766, 0, 2400609, 607383, 144615, 1966764, 0, 636306, 2487378, 28923, 
              1793226, 694152, 780921, 173538, 173538, 491691, 173538, 751998, 1475073, 
              925536, 1417227, 751998, 202461, 347076, 491691]

    # Calculate shared key (same as in encryption)
    u = generator(g, a, p)
    v = generator(g, b, p)
    shared_key = generator(v, a, p)
    print(f"Shared key: {shared_key}")  # Debug info

    # First decrypt using the shared key
    semi_plain = decrypt(cipher, shared_key)
    print(f"After first decryption: {semi_plain}")  # Debug info
    
    # Then decrypt using XOR with the text key
    plain_text = dynamic_xor_decrypt(semi_plain, text_key)
    
    return plain_text

if __name__ == "__main__":
    decrypted_message = decrypt_message()
    reversed_decrypted_message = decrypted_message[::-1]
    print(f"Decrypted message: {reversed_decrypted_message}")

