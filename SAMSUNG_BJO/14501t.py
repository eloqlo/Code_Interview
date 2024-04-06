if __name__ == "__main__":
    n = int(input())
    data = [[0, 0]]
    dp = [0 for _ in range(n+2)]
    res = 0

    for _ in range(n):
        data.append((list(map(int, input().split()))))

    for i in range(1, n+1):
        nxt = i + data[i][0]
        # 다음 상담이 가능한 모든 상담 일자의 dp값 갱신
        for j in range(nxt, n+2):
            dp[j] = max(dp[j], dp[i] + data[i][1])
            print(dp)
        print()

    print(dp[n+1])
