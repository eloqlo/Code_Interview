"""
RGB 거리

제일 작은 놈에서부터 저 조건을 성립하는 놈까지 거꾸로 올라가면 될듯?
3 * 2^(N-1) 경우의 수 -> 3개의 BT?
https://m.blog.naver.com/ndb796/221233560789
BT traversal 로 해결해보자. 시간제한 걸리려나? 아직도 뭔가 무식한 방식같은데...
어차피 통과만 하면 되는 코테, 너무 신경쓰진 말자.

#################

- sum 하면서, 각 집 별로 칠한 숫자 인덱스를 저장한다.
    - 집 돌면서, 
        1. 작은 숫자 순서대로 n원소들의 인덱스를 저장
- 가장 작은놈부터 제시된 조건을 만족하는지 해본다.
    - test_function(attrdict(house_num : idx))
"""
import sys

n = int(input())

price = []
for _ in range(n):
    price.append(list(map(int,sys.stdin.readline().strip().split())))

