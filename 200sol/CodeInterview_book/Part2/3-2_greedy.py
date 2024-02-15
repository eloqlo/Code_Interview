# 큰 수의 법칙
"""
정답과 같은 방식의 접근
"""
import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
li = [i for i in map(int, input().split())]     # input()을 split()한게 generator이라 map써서 할 수 있고, map객체가 반환하는게 iterable이니깐 list comprehension으로 쓸 수 있지.
result = 0

#1 가장 큰 수와 그다음 크거나 같은 수를 찾는다.
#2 큰걸K번, 작은걸 1번을 M번 더해준다.

li_sorted = sorted(li, reverse=True)
max_val, next_max_val = li_sorted[0], li_sorted[1]

for i in range(1,M+1):
    if i%(K+1)==0:
        result += next_max_val
    else:
        result += max_val
    
    print(result)


print(result)