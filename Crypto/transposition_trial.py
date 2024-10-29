#!/usr/bin/env python3

with open("message.txt", "r") as f:
    lines = f.read()

for i in range(0, len(lines), 3):
    s = lines[i : i + 3] 
    a, b, c = s
    p = c + a + b
    print(p, end="")
