def pm(arr):
    for l in arr:
        for e in l:
            print(e,end=' ')
        print()
    print('_____')

def dfs(vl,previ):
    global M, NUM_OF_VIRUS, v, min_time
    if len(vl)==M:
        time = bfs(vl)
        if time == -1:
            return
        elif time < min_time:
            min_time = time
            return
    for idx in range(previ+1,NUM_OF_VIRUS):
        dfs(vl + [v[idx]], idx)

def bfs(v):
    global arr,N,blk
    arrt = [l.copy() for l in arr]
    blkt = blk
    visited = [[False] * N for _ in range(N)]
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    for time in range(2500):
        nv=[]
        while v:
            r,c = v.pop()
            visited[r][c]=True
            if arrt[r][c]=='^':
                blkt-=1
            if blkt==0:
                return time
            arrt[r][c]=time
            for di in range(4):
                nr = r+dr[di]
                nc = c+dc[di]
                if 0<= nr <=N-1 and 0<= nc <=N-1:
                    if arrt[nr][nc]=='^' and visited[nr][nc]==False:
                        nv.append((nr,nc))
                        visited[nr][nc]=True
                    elif arrt[nr][nc]=='*' and visited[nr][nc]==False:
                        nv.append((nr,nc))
                        visited[nr][nc] = True
        v=nv
        if len(v)==0:
            break
    return -1

N,M=map(int,input().split())
arr=[]
v=[]
blk=0
for r in range(N):
    arr.append([])
    for c, ele in enumerate(list(map(int, input().split()))):
        if ele==0:
            arr[r].append('^')
            blk+=1
        elif ele==1:
            arr[r].append('-')
        elif ele==2:
            arr[r].append('*')
            v.append((r,c))
min_time=1000000
NUM_OF_VIRUS=len(v)
if blk==0:
    print(0)
else:
    dfs([],-1)
    if min_time==1000000:
        print(-1)
    else:
        print(min_time)