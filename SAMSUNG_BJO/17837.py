def solution():
    global N, K, board, totems,tboard
    dr=[0,0,-1,1]
    dc=[1,-1,0,0]
    turn=0
    while 1:
        if turn==1000:
            break
        turn += 1
        for k_idx in range(len(totems)):
            r, c, d, k = totems[k_idx]
            nr,nc = r+dr[d], c+dc[d]
            if board[nr][nc] >= 2:    # blue / wall
                nd = reverse_di(d)
                totems[k][2]=nd
                nr,nc = r+dr[nd], c+dc[nd]
                if board[nr][nc]>=2:
                    continue
                else:
                    is_end = red_white(r,c,nd,k,board[nr][nc])
                    if is_end:
                        return turn
                    continue
            else:
                is_end = red_white(r, c, d, k, board[nr][nc])
                if is_end:
                    return turn
                continue
    return -1

def red_white(r,c,d,k,color):
    if color>1:
        raise Exception("color error")
    global totems,tboard
    dr=[0,0,-1,1]
    dc=[1,-1,0,0]
    nr, nc = r+dr[d], c+dc[d]
    k_i = tboard[r][c].index(k)     # 기존 위치에서 업힌애들 데려오기
    tmp = tboard[r][c][k_i:]
    for k_upper_i in tmp:
        totems[k_upper_i][0], totems[k_upper_i][1] = nr,nc  # 업힌거 위치 수정
    tboard[r][c] = tboard[r][c][:k_i]
    if color==1:
        tmp.reverse()
    tboard[nr][nc] += tmp

    return len(tboard[nr][nc])>=4

def reverse_di(d):
    if d==0:
        return 1
    elif d==1:
        return 0
    elif d==2:
        return 3
    elif d==3:
        return 2


N,K = map(int,input().split())
board = [[3]*(N+2)]
for _ in range(N):
    board.append([3] + list(map(int, input().split())) + [3])
board.append([3]*(N+2))
tboard = []
for _ in range(N+2):
    tboard.append([[] for _ in range(N+2)])
totems=[]
for k in range(K):
    r,c,d=map(int,input().split())
    totems.append([r,c,d-1,k])
    tboard[r][c].append(k)
print(solution())