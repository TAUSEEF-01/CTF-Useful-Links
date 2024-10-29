# This code is applicable when e = 1

from sympy import gcd, mod_inverse
from sympy.ntheory import factorint

# Given values
e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083

m = pow(c, 1, n) # when e = 1

# Display the result in text format
message = bytearray.fromhex(hex(m)[2:]).decode()
print("Decrypted Message:", message)
