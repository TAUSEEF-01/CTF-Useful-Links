from pwn import *
from Crypto.Util.number import *

def parse_parameters(conn):
    conn.recvuntil(b"n: ")
    n = int(conn.recvline().strip())
    conn.recvuntil(b"e: ")
    e = int(conn.recvline().strip())
    conn.recvuntil(b"ciphertext: ")
    ct = int(conn.recvline().strip())
    return n, e, ct

try:
    # Connect to server
    conn = remote('mercury.picoctf.net', 2671)
    
    # Get parameters from server
    n, e, ct = parse_parameters(conn)
    
    # Choose random value r and compute modified ciphertext
    r = 2
    r_e = pow(r, e, n)
    modified_ct = (ct * r_e) % n
    
    # Send modified ciphertext
    conn.sendlineafter(b"decrypt: ", str(modified_ct).encode())
    
    # Parse response
    response_line = conn.recvline().decode()
    response = int(response_line.split("Here you go: ")[1].strip())
    
    # Recover original message
    message = (response * pow(r, -1, n)) % n
    
    # Convert to bytes and print
    flag = long_to_bytes(message)
    print(f"\nDecrypted message: {flag.decode()}")

except Exception as e:
    print(f"Error: {e}")
finally:
    try:
        conn.close()
    except:
        pass
