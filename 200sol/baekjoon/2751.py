import sys
n = int(input())

li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().strip()))

li.sort()

for i in li:
    print(i)    