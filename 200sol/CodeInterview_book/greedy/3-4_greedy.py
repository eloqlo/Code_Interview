# 1이 될 때까지 p.99
"""
빼는것보단 나누는게 항상 더 빠를까?
공약수가 계속 바뀐다.

>>> 나누는게 더 빠르기때문에 나누었다고만 설명했다.
"""
import sys

N, K = map(int,sys.stdin.readline().split())

count = 0

while N!=1:
    if N<K:
        count += N-1
        break
    
    remainder = N%K
    count += remainder
    N -= remainder
    N /= K
    count+=1

print(int(count))