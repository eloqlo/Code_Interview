# 파이썬을 위한 문제는 아니긴 하군.
# 하지만 풀 수 있구나.

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().strip().split())
li = list(map(int,sys.stdin.readline().strip().split()))

tmp = deque()
count = 0
hi=0

while True:
    if hi==n:
        break
    tmp.append(li[hi])
    hi+=1

    if sum(tmp)==m:
        count+=1
        tmp.popleft()
    elif sum(tmp)>m:
        if len(tmp)==1:
            tmp.pop()
            continue
        tmp.popleft()
        tmp.pop()
        hi-=1

print(count)