# # N = int(input())
# # arr=[]
# # for _ in range(N):
# #     arr.append(tuple(map(int,input().split())))
# # margin=[0]*(N+1)
#
# def solution(N, arr):
#     margin = [0] * (N + 1)
#     for i in range(N):
#         ti, pi = arr[i]
#         if i+ti <= N:
#             margin[i+ti] = max(margin[i+ti], margin[i] + pi)
#     return max(margin)
#
# T = int(input())
# answers=[]
# for t in range(T):
#     N = int(input())
#     arr = []
#     for _ in range(N):
#         arr.append(tuple(map(int, input().split())))
#     answers.append(solution(N,arr))
#
# for i, answer in enumerate(answers):
#     print(f"#{i+1} {answer}")

N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

def solution(N, arr):
    margin = [0] * (N+1)      # margin[i]는 i일 까지 최대 이익
    for i in range(N):
        ti, pi = arr[i]
        if i+ti <= N:
            for j in range(i+ti, N+1):
                margin[j] = max(margin[j], margin[i]+pi)
    return max(margin)

print(solution(N,arr))