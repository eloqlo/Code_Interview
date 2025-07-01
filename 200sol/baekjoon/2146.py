def solution():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int,input().split())))

    visit = [[0]*N for _ in range(N)]
    island = []
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    for r in range(N):
        for c in range(N):
            if A[r][c]==1:
                visit[r][c]=1
