"""
RGB 거리

n개의 집중 제일 작은 애부터 선택을 해주고, 그다음 작은애가 앞뒤 인덱스와 다르면 그거로 선택, 아니면 그다음 작은애 선택.
만일 작은 값이 같으면... 거기서 분기점 나눠서 계산 해주고 전체 중에서 제일 작은 값을 선택하면 될듯?
- 제일 작은 price 부터 선택을 한다.
- 그다음 작은애가 앞뒤 인덱스와 다르면

뭐지.. 일단 풀어봐?
"""
import sys

n = int(input())

price = []
for _ in range(n):
    price.append(list(map(int,sys.stdin.readline().strip().split())))

