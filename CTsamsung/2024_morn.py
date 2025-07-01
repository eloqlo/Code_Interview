from collections import deque

def rot(A,r,c,rot_idx):
    tmp = []
    tmp.append(A[r-1][c-1:c+2])
    tmp.append(A[r][c-1:c+2])
    tmp.append(A[r+1][c-1:c+2])
    A_new =[line.copy() for line in A]
    if rot_idx==0:
        # rot 90
        tmp.reverse()
        tmp=list(zip(*tmp))
    elif rot_idx==1:
        # rot 180
        tmp.reverse()
        tmp = list(zip(*tmp))
        tmp.reverse()
        tmp = list(zip(*tmp))
    elif rot_idx==2:
        # rot 270
        tmp = list(zip(*tmp))
        tmp.reverse()
    A_new[r - 1][c - 1:c + 2] = tmp[0]
    A_new[r][c - 1:c + 2] = tmp[1]
    A_new[r + 1][c - 1:c + 2] = tmp[2]
    return A_new

def bfs(A):

    visit = [[0]*5 for _ in range(5)]
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    chunk_locs = []
    for r in range(5):
        for c in range(5):
            if visit[r][c]==1:
                continue
            visit[r][c]=1
            dq=[(r,c)]
            cur_chunk_locs = [(r,c)]
            cur_num = A[r][c]
            while dq:
                tmpr, tmpc = dq.pop()
                for di in range(4):
                    nr,nc = tmpr+dr[di], tmpc+dc[di]
                    if 0<=nr<5 and 0<=nc<5:
                        if A[nr][nc]==cur_num and visit[nr][nc]==0:
                            visit[nr][nc] = 1
                            dq.append((nr,nc))
                            cur_chunk_locs.append((nr,nc))
            if len(cur_chunk_locs)>=3:
                chunk_locs+=cur_chunk_locs

    return chunk_locs

def p(A):
    for l in A:
        for e in l:
            print(e,end=' ')
        print()
    print()

def solution():
    K, M = map(int, input().split())
    A = []
    for _ in range(5):
        A.append(list(map(int, input().split())))
    nxt_objects = deque(list(map(int, input().split())))
    answer = []

    for k_num in range(K):
        # 회전각도, 열, 행
        COUNT = 0
        max_chunks = 0
        max_chunk_locs = []
        max_A = None
        max_r, max_c = None, None

        for rot_idx in [0,1,2]:
            for cen_c in [1,2,3]:
                for cen_r in [1,2,3]:
                    A_tmp = rot(A, cen_r, cen_c, rot_idx)
                    chunks = bfs(A_tmp)

                    if len(chunks) > max_chunks:
                        max_chunks = len(chunks)
                        max_r, max_c, rot_i = cen_r, cen_c, rot_idx
                        max_chunk_locs = chunks
                        max_A = A_tmp

        if max_A==None: # NO UPDATES
            break
        # print("after first, ", len(max_chunk_locs))
        # print(max_chunk_locs)
        # p(max_A)
        # print("max_r,max_c,rot_i ",max_r,max_c,rot_i)

        max_chunk_locs.sort(key=lambda x:(x[1],-x[0]))
        for mr, mc in max_chunk_locs:
            max_A[mr][mc] = nxt_objects.popleft()
        COUNT += len(max_chunk_locs)

        while 1:
            chunk_locs = bfs(max_A)
            if len(chunk_locs)==0:
                break
            chunk_locs.sort(key=lambda x: (x[1], -x[0]))

            # print("뒤처리중... ", len(chunk_locs))
            # print(chunk_locs)
            # p(max_A)

            for mr, mc in chunk_locs:
                max_A[mr][mc] = nxt_objects.popleft()
            COUNT += len(chunk_locs)
        A = max_A
        answer.append(COUNT)
        # print("______________________________")

    for count in answer:
        print(count, end=' ')

solution()