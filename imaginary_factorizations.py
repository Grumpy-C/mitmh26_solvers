# original file name: mitfactorization.py
import math

inp = 7152154301 # example value
min = math.floor(math.sqrt(inp))

for i in range(min, 0, -1):
    b = math.sqrt(inp - i**2)
    if abs(b - round(b)) < 0.0000001: # avoid floating point problems

        print(i, b)
