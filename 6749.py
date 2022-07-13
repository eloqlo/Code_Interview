from re import L
import sys

input = []
for _ in range(4):
    input.append(int(sys.stdin.readline().strip()))

s = sum(input)

print(s//60)
print(s%60)