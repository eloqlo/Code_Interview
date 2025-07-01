# # 입력을 테스트케이스에 대해 list로 저장
# t = int(input())
# m=[0 for _ in range(t)]
# n=[0 for _ in range(t)]
# k=[0 for _ in range(t)]
# pos=[[] for _ in range(t)]
# passed=[[] for _ in range(t)]
# for i in range(t):
#     m[i],n[i],k[i] = map(int,input().split())
#     for _ in range(k[i]):
#         pos[i].append(list(map(int,input().split())))
#
#
# # 각 테스트케이스에 대해 반복
# for i in range(t):
#     ans=[]
#     ans.append(pos[i][0])   # 고립된 좌표들
#     passed[i].append(pos[i][0])    # 첫 좌표 추가
#
#     for p in pos[i][1:]:
#         # 지나온애 내부중 새로운애의 상하좌우 겹치는지 조회
#         flag=False
#         if p[0] > 0:
#             if [p[0]-1,p[1]] in passed[i]: flag=True
#         if p[0] < m[i]-1:
#             if [p[0]+1,p[1]] in passed[i]: flag=True
#         if p[1] > 0:
#             if [p[0],p[1]-1] in passed[i]: flag=True
#         if p[1] < n[i]-1:
#             if [p[0],p[1]+1] in passed[i]: flag=True
#         passed[i].append(p) # 지나온 애들에 추가
#
#         # 지나온 좌표들과 겹치지 않으면 ans에 추가
#         if not flag:
#             ans.append(p)
#     # ans내부에서 겹치는지 확인
#     real_ans=[]
#     for p in ans:
#         flag=False
#         if p[0] > 0:
#             if [p[0]-1,p[1]] in ans: flag=True
#         if p[0] < m[i]-1:
#             if [p[0]+1,p[1]] in ans: flag=True
#         if p[1] > 0:
#             if [p[0],p[1]-1] in ans: flag=True
#         if p[1] < n[i]-1:
#             if [p[0],p[1]+1] in ans: flag=True
#
#         if not flag:
#             real_ans.append(p)
#
#     print(len(real_ans))



def solution():
    global N,M, arr, loc

    count = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                count += 1
                # dfs(r,c)
                make_zero(r,c)

    return count

def make_zero(r,c):
    global arr, N, M
    stack=[(r,c)]

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    while stack:
        r,c = stack.pop()
        arr[r][c] = 0
        for di in range(4):
            nr = r + dr[di]
            nc = c + dc[di]
            # 동서남북 확인, 미방문 시 방문
            if 0 <= nr <= N - 1 and 0 <= nc <= M - 1:
                if arr[nr][nc] == 1:
                    stack.append((nr,nc))


# 제귀 깊이가 2000을 넘을 수 있기에 X
def dfs(r,c):
    global arr, N, M
    # 방문처리
    arr[r][c]=0

    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    for di in range(4):
        nr = r + dr[di]
        nc = c + dc[di]
        # 동서남북 확인, 미방문 시 방문
        if 0<=nr<=N-1 and 0<=nc<=M-1:
            if arr[nr][nc]==1:
                dfs(nr,nc)

import time

# main
T = int(input())
answers=[]
for _ in range(T):
    M,N,K = map(int,input().split())
    arr=[[0]*M for _ in range(N)]
    for _ in range(K):
        x,y = map(int,input().split())
        arr[y][x] = 1

    st = time.time()
    answers.append(solution())
    ed = time.time()
    # print(f"execution time - {ed-st}s")

for ans in answers:
    print(ans)

