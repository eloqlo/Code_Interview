def solution():
    M, N = map(int, input().split())
    A = []
    tmt_loc = []
    blue_tmt = 0
    for r in range(N):
        line=[]
        for c,ele in enumerate(map(int,input().split())):
            if ele==1:
                tmt_loc.append((r,c))
            elif ele==0:
                blue_tmt+=1
            line.append(ele)
        A.append(line)

    date_count = 0
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    visit = [[0]*M for _ in range(N)]
    for _ in range(N*M):
        if blue_tmt==0:
            return date_count
        if len(tmt_loc)==0:
            return -1

        nxt_tmt = []
        while tmt_loc:
            r,c = tmt_loc.pop()

            for di in range(4):
                nr, nc = r+dr[di], c+dc[di]
                if 0<=nr<N and 0<=nc<M:
                    if A[nr][nc]==0 and visit[nr][nc]==0:
                        blue_tmt-=1
                        visit[nr][nc]=1
                        A[nr][nc]=1
                        nxt_tmt.append((nr,nc))

        tmt_loc = nxt_tmt
        date_count += 1

print(solution())