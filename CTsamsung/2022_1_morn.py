def solution():

    # INPUTS
    N,M,H,K = map(int,input().split())
    A = [[[] for _ in range(N)] for _ in range(N)]
    runners = {}
    for m in range(M):
        x,y,d = map(int, input().split())
        runners[m+1] = [x-1,y-1,d,0]
        A[x-1][y-1].append(m+1)
    # trees = set()
    T = [[0]*N for _ in range(N)]
    for _ in range(H):
        x,y = map(int,input().split())
        # trees.add((x-1,y-1))
        T[x-1][y-1] = 1
    sx,sy,sd = N//2, N//2, 0

    sdx = [-1, 0, 1, 0]
    sdy = [0, 1, 0, -1]
    rdx = {1:[0,0], 2:[1,-1]}   # 1좌우 2하상
    rdy = {1:[1,-1], 2:[0,0]}
    SCORE = 0

    # [OK]
    gen_catcher_loc = get_catcher_loc(N)

    # print("START")
    # pp(A,T,sx,sy)

    for turn in range(1,K+1):
        # get moving runners [OK]
        moving_runners = get_moving_runners(A,sx,sy)

        # runners move [OK]
        for ri in moving_runners:
            x,y,d1,d2 = runners[ri]
            nx, ny = x+rdx[d1][d2], y+rdy[d1][d2]
            if 0<=nx<N and 0<=ny<N:
                if (nx,ny)==(sx,sy):
                    continue
                runners[ri] = [nx,ny,d1,d2]
                A[x][y].remove(ri)
                A[nx][ny].append(ri)
            else:
                d2 = (d2+1)%2
                nx, ny = x + rdx[d1][d2], y + rdy[d1][d2]
                if (nx,ny)==(sx,sy):
                    runners[ri][3] = d2
                    continue
                runners[ri] = [nx,ny,d1,d2]
                A[x][y].remove(ri)
                A[nx][ny].append(ri)

        # print("AF MOVE")
        # pp(A,T,sx,sy)

        # catcher move
        sx, sy, sd = next(gen_catcher_loc)
        catched = []
        for foo in range(3):
            nsx, nsy = sx+sdx[sd]*foo, sy+sdy[sd]*foo
            if 0<=nsx<N and 0<=nsy<N and T[nsx][nsy]==0:
                catched += A[nsx][nsy]
        for cri in catched:
            x, y, d1, d2 = runners[cri]
            A[x][y] = []
            runners[cri] = None
        SCORE += turn * len(catched)

        # print()
        # print("AF S MOVE")
        # if catched:
        #     print('----------',len(catched),"*",turn)
        # print(catched)
        # pp(A,T,sx,sy)
        # print("____________________")
        # input()

    return SCORE


# OK
def get_catcher_loc(N):

    sdx = [-1, 0, 1, 0]
    sdy = [0, 1, 0, -1]

    while 1:
        sx, sy, sd = N // 2, N // 2, 0
        backup_loc = [(sx,sy)]
        backup_d = [sd]
        count = 1
        while 1:
            for _ in range(2):
                for steps in range(count):
                    sx = sx + sdx[sd]
                    sy = sy + sdy[sd]
                    if steps == count-1:
                        sd = (sd + 1) % 4
                    if (sx,sy)==(0,0):
                        sd = 2  # DOWN
                        yield sx, sy, sd
                        backup_d.pop()
                        break

                    backup_loc.append((sx,sy))
                    backup_d.append(sd)
                    yield sx,sy,sd
                if (sx,sy)==(0,0):
                    break
            if (sx,sy)==(0,0):
                break
            count+=1

        backup_loc.reverse()
        backup_d.reverse()
        new_backup_d = []
        for ele in backup_d:
            new_backup_d.append((ele+2)%4)
        new_backup_d.append(0)
        backup_d = new_backup_d
        for (sx,sy), sd in zip(backup_loc, backup_d):
            yield sx,sy,sd

# OK
def get_moving_runners(A,sx,sy):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    N = len(A)
    MAX_MOVE = 3
    dq = [(sx,sy)]
    B = [[0]*N for _ in range(N)]
    B[sx][sy] = 1

    moving_runners = []
    if A[sx][sy]:
        moving_runners += A[sx][sy]

    for _ in range(MAX_MOVE):
        nxt_dq = []
        for x,y in dq:
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                if 0<=nx<N and 0<=ny<N and B[nx][ny]==0:
                    nxt_dq.append((nx,ny))
                    B[nx][ny] = 1
                    if len(A[nx][ny])>0:
                        moving_runners += A[nx][ny]
        dq = nxt_dq

    return moving_runners

def pp(A,T,sx,sy):
    for x,l in enumerate(A):
        for y,e in enumerate(l):
            if T[x][y]==1:
                print("*",end='')
            if (x,y)==(sx,sy):
                print("S",end='')
            if len(e)>0:
                print(','.join(list(map(str,e))), end = '\t')
            else:
                print('.', end='\t')
        print()

def p(B):
    for l in B:
        for e in l:
            print(e, end='\t')
        print()


# N = int(input())
# M = int(input())
# A = [[[] for _ in range(N)] for _ in range(N)]
# for m in range(M):
#     x,y = map(int,input().split())
#     A[x][y].append(m+1)
# pp(A)
#
# print(get_moving_runners(A, len(A)//2, len(A)//2))

print(solution())