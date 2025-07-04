from collections import deque

def solution(arr,L,R):
    N = len(arr)
    day = 0
    for _ in range(1, 2001):
        # get unions
        cur_unions_arr = []
        visit = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                union = union_finder(visit, r,c)
                if len(union)>=2:
                    cur_unions_arr.append(union)
        # end condition - no union
        if len(cur_unions_arr)==0:
            break
        day += 1
        # adjust map
        for cur_union in cur_unions_arr:
            bunja=0
            bunmo=len(cur_union)
            for r,c in cur_union:
                bunja+=arr[r][c]
            new_pop = bunja//bunmo
            for r,c in cur_union:
                arr[r][c] = new_pop
    return day

def union_finder(visit, r,c):
    global N,L,R
    dq = deque()
    dq.append((r,c))
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    union = []
    if visit[r][c]:
        return union
    visit[r][c] = 1
    while dq:
        cur_r,cur_c = dq.popleft()
        union.append((cur_r,cur_c))
        for di in range(4):
            nr = cur_r + dr[di]
            nc = cur_c + dc[di]
            if 0<=nr<N and 0<=nc<N:
                if visit[nr][nc]!=1 and L<=abs(arr[nr][nc]-arr[cur_r][cur_c])<=R:
                    dq.append((nr,nc))
                    visit[nr][nc]=1
    return union

N,L,R = map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))

print(solution(arr,L,R))