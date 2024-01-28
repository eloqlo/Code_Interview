# 예제 3-1 거스름돈 : 내 풀이
"""
나머지를 생각했었다면 더 간단했겠군.
"""

N = int(input())

counter = []

# 큰 수부터 나눠 몫을 구해준다.
counter.append(N//500)
N -= counter[0]*500
counter.append(N//100)
N -= counter[1]*100
counter.append(N//50)
N -= counter[2]*50
counter.append(N//10)

del N

print(counter)
print(sum(counter))

##############################################
# 답 풀이

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n//coin
    n %= coin

print(count)