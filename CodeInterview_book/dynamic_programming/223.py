
def solution(n):
    result=0
    dp = [0,1,3]

    #1 n-1까지 f(n-k)값들 구하자
    for idx in range(3,n+1):
        dp.append(dp[idx-1] + dp[idx-2]*2)

    return dp[n] % 796796


N = int(input())
print(solution(N))