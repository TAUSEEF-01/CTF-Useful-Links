#03464b4f1a1c3a313d1951573d195102383d1907533d1905033d1904043d1904
#51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57

#xor decryption

a = 0x51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57 # hex val    
b = 0x03464b4f1a1c3a313d1951573d195102383d1907533d1905033d1904043d1904
c = 0x6161616161616161616161616161616161616161616161616161616161616161

#'{:x}'.format(a ^ b ^ c)
print('{:x}'.format(a ^ b ^ c))
