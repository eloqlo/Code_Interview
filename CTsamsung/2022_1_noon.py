def get_ball_hit_coord(A,k):

    N = len(A)
    anchor1 = (k // N)%4
    anchor2 = k % N

    if anchor1 >= 2:
        anchor2 = (N - 1) - anchor2

    search = [i for i in range(N)]
    if anchor1 in (1, 2):
        search.reverse()

    if anchor1%2==0:    # row wise
        for idx in search:
            if A[anchor2][idx] in (1,2,3):
                return anchor2, idx
    else:   # col wise
        for idx in search:
            if A[idx][anchor2] in (1,2,3):
                return idx, anchor2
    return -1,-1

def find_head(A, r, c):

    N = len(A)
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    if A[r][c] == 1:
        return 1, r, c

    dq = [(r,c)]
    visit = set((r,c))
    pos = 1
    while dq:
        nxt_dq = []
        for cr, cc in dq:
            for di in range(4):
                nr, nc = cr + dr[di], cc + dc[di]
                if 0 <= nr < N and 0 <= nc < N and A[nr][nc] in (1,2) and (nr,nc) not in visit:
                    if A[cr][cc]==3 and A[nr][nc]==1:
                        continue
                    if A[nr][nc] == 1:
                        return pos+1, nr,nc
                    nxt_dq.append((nr,nc))
                    visit.add((nr,nc))
        dq = nxt_dq
        pos += 1

def p(A):
    for l in A:
        for e in l:
            if e==0:
                print('.', end=' ')
            elif e==4:
                print('#', end=' ')
            else:
                print(e, end=' ')
        print()
    print()
def solution():

    # CONFIGS
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    SCORE = 0
    N,M,K = map(int,input().split())
    group = {}
    A = []
    for r in range(N):
        line = list(map(int,input().split()))
        A.append(line)
        for c in range(N):
            if line[c]==1:
                group[(r,c)] = None
    for r,c in group.keys():
        visit = set((r,c))
        dq = [(r,c)]
        tr,tc = -1, -1
        while dq:
            cr, cc = dq.pop()
            for di in range(4):
                nr, nc = cr + dr[di], cc + dc[di]
                if 0 <= nr < N and 0 <= nc < N and A[nr][nc] in (2,3) and (nr,nc) not in visit:
                    if A[nr][nc] == 3:
                        tr,tc = nr,nc
                        dq=[]
                        break
                    else:
                        visit.add((nr, nc))
                        dq.append((nr, nc))
        if tr == -1:
            raise Exception()
        group[(r, c)] = (tr, tc)


    # ROUNDS
    # print("INITAL")
    # p(A)
    # input()
    for k in range(K):
        # print(f"_______________R {k+1}_______________")

        # GROUP MOVE
        new_group = {}
        for hr,hc in group.keys():
            tr,tc = group[(hr,hc)]
            new_hr,new_hc = -1,-1
            new_tr,new_tc = -1,-1
            for di in range(4):
                nhr,nhc = hr + dr[di], hc + dc[di]
                if 0<=nhr<N and 0<=nhc<N and A[nhr][nhc] in (4,3):
                    new_hr, new_hc = nhr,nhc
            for di in range(4):
                ntr,ntc = tr + dr[di], tc + dc[di]
                if 0<=ntr<N and 0<=ntc<N and A[ntr][ntc]==2:
                    new_tr, new_tc = ntr, ntc
            new_group[(new_hr,new_hc)] = (new_tr, new_tc)
            A[tr][tc] = 4
            A[hr][hc] = 2
            A[new_tr][new_tc] = 3
            A[new_hr][new_hc] = 1
        group = new_group

        # print("AF MOVE")
        # p(A)
        # input()

        # BALL SHOOTING
        br, bc = get_ball_hit_coord(A, k)
        if br == -1:
            # p(A)
            # input()
            continue

        pos, hr, hc = find_head(A, br, bc)
        tr, tc = group[(hr,hc)]
        group.pop((hr,hc))
        group[(tr,tc)] = (hr,hc)
        A[hr][hc] = 3
        A[tr][tc] = 1

        # print(f"{br,bc}에 맞음 {pos}번째, 반전됨!")
        # print(f"SCORE ++ {pos**2}")
        # p(A)
        # input()
        SCORE += pos**2


    return SCORE


print(solution())
