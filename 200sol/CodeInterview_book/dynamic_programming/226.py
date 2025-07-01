N,M = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

def solution(M, coins):
    arr = [10001]*(10001)   # 40kb
    for c in coins:
        arr[c] = 1

    for idx in range(1, M+1):
        for coin in coins:
            if idx-coin < 1:
                continue
            else:
                arr[idx] = min(arr[idx-coin]+1, arr[idx])

    if arr[M]==10001:
        return -1
    else:
        return arr[M]


print(solution(M, coins))