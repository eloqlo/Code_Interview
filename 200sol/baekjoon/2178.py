N,M = map(int,input().split())
A=[]
for _ in range(N):
    A.append(list(map(int,input())))


def solution():
    global A,N,M
    visit = [[0]*M for _ in range(N)]
    visit[0][0]=1
    dq=[(0,0)]
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    count=1

    while dq:
        nxt_dq=[]
        for idx in range(len(dq)):
            r,c = dq[idx]
            for di in range(4):
                nr,nc = r+dr[di], c+dc[di]
                if 0<=nr<N and 0<=nc<M:
                    if A[nr][nc]==1 and visit[nr][nc]==0:
                        visit[nr][nc]=1
                        if (nr,nc)==(N-1,M-1):
                            return count+1
                        nxt_dq.append((nr,nc))
        dq = nxt_dq
        count+=1

print(solution())