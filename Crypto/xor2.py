# Single-byte XOR cipher


import binascii
from collections import Counter

def single_byte_xor_cipher(hex_string):
    # Convert hex string to bytes
    bytes_data = binascii.unhexlify(hex_string)
    
    # Score text based on frequency of English letters
    def score_text(text):
        # Frequency of common characters in English
        character_frequencies = {
            'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442,
            'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033,
            'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302,
            'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357,
            'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984,
            'z': 0.0007836, ' ': 0.1918182
        }
        
        return sum([character_frequencies.get(chr(byte), 0) for byte in text.lower()])

    # Try each possible byte (0x00 to 0xFF) as the key
    best_score = 0
    best_result = None
    best_key = None
    
    for key in range(256):
        # XOR each byte with the key
        decoded = bytes([b ^ key for b in bytes_data])
        
        # Score the result
        score = score_text(decoded)
        
        # Keep track of the best result
        if score > best_score:
            best_score = score
            best_result = decoded
            best_key = key

    # Return the best result and key
    return best_result.decode("utf-8", errors="ignore"), best_key

# Example usage
hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736" # The hex encoded string here
decoded_text, key = single_byte_xor_cipher(hex_string)
print("Decoded Text:", decoded_text)
print("Key:", key)
