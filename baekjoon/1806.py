import sys
from collections import deque

n,s = map(int,input().split())
li = [n for n in map(int, sys.stdin.readline().strip().split())]

front = 0
back = 0

for i in range(n):
    