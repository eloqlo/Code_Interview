def bfs(maps):
    dr = [0,1,-1,0]
    dc = [1,0,0,-1]
    
    N = len(maps)
    M = len(maps[0])
    counter = 1
    visit = [[0]*M for _ in range(N)]
    visit[0][0] = 1
    q = [(0,0)]
    while q:
        counter += 1
        nxt = []
        for cr,cc in q:
            for di in range(4):
                nr,nc = cr+dr[di],cc+dc[di]
                if 0<=nr<N and 0<=nc<M and maps[nr][nc]>0 and visit[nr][nc]==0:
                    if (nr,nc) == (N-1,M-1):
                        return counter
                    visit[nr][nc] = 1
                    maps[nr][nc] = counter
                    nxt.append((nr,nc))
        q = nxt
    return -1


def solution(maps):
    dist = bfs(maps)
    print(dist)
    for line in maps:
        for e in line:
            print(e,end=' ')
        print()
    print("___________")
    return dist


val = [[1,1,1,1]]


solution(val)