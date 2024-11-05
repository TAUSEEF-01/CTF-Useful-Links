"""
    CBC Bit Flipping is an attack that exploits the Cipher Block Chaining (CBC) encryption mode by modifying ciphertext to alter the corresponding plaintext upon decryption.
"""

import requests
import base64

s = requests.Session()
s.get("http://mercury.picoctf.net:21553/")
cookie = s.cookies["auth_name"]
print(cookie)
unb64 = base64.b64decode(cookie)
print(unb64)

unb64b = base64.b64decode(unb64)

for i in range(0, 128):
    pos = i // 8
    # XOR the byte directly
    modified_byte = unb64b[pos] ^ (1 << (i % 8))
    # Reconstruct the modified byte string
    guessdec = unb64b[:pos] + bytes([modified_byte]) + unb64b[pos + 1:]
    # Double encode the modified guess and decode to string
    guessenc1 = base64.b64encode(guessdec)
    guess = base64.b64encode(guessenc1).decode('utf-8')

    r = requests.get("http://mercury.picoctf.net:21553/", cookies={"auth_name": guess})
    if "pico" in r.text:
        print(r.text)
