def solution(N, M, arr):
    print(arr)
    ans = [0]*(N+2)
    for row in range(N):
        ans[row+1] = arr[row][0]

    for col in range(1,M):
        new_ans = [0]*(N+2)
        for row in range(N):
            new_ans[row+1] = max(ans[row], ans[row+1], ans[row+2]) + arr[row][col]
        ans = new_ans
    return max(ans)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
T = int(input())
answers=[]
for _ in range(1,T+1):
    N,M = map(int, input().split())
    tmp = list(map(int, input().split()))
    arr = []
    for foo in range(N):
        arr.append(tmp[foo*M:foo*M+M])
    answers.append(solution(N,M,arr))

for tc, answer in enumerate(answers):
    print(f"#{tc+1} {answer}")