def pm(board):
    for l in board:
        for e in l:
            print(e,end='\t')
        print()
    print('--------')

def solution():
    dr = [None,-1,1,0,0]
    dc = [None,0,0,-1,1]
    N,M,k = map(int,input().split())
    cur_shark_di = [0]*(M+1)
    shark_di_dict= [0]*(M+1)
    board = [[] for _ in range(N)]
    for r in range(N):
        for ele in map(int,input().split()):
            if ele==0:
                board[r].append(ele)
            else:
                board[r].append([ele,k])
    for si_, di in enumerate(map(int,input().split())):
        cur_shark_di[si_+1] = di
    for si_ in range(M):
        order = []
        for _ in range(4):
            order.append(list(map(int,input().split())))
        shark_di_dict[si_+1] = order

    for time in range(1,1002):

        # 살아있는 상어 조회
        cur_sharks=[]
        for r in range(N):
            for c in range(N):
                if board[r][c]==0:
                    continue
                else:
                    si, sec = board[r][c]
                    if sec==k:
                        cur_sharks.append([si,r,c])
        if len(cur_sharks)==1:
            return time-1

        # 상어들 이동할 곳 찾아주기
        nxt_shark_loc = []
        for si, sr, sc in cur_sharks:
            cur_d = cur_shark_di[si]
            nxt_d_list = shark_di_dict[si][cur_d-1]

            # find next location
            passit = False
            for ndi in nxt_d_list:
                nr, nc = sr+dr[ndi], sc+dc[ndi]
                if 0 <= nr <= N - 1 and 0 <= nc <= N - 1:
                    if board[nr][nc]==0:
                        nxt_shark_di = ndi
                        passit = True
                        break
            if not passit:
                for ndi in nxt_d_list:
                    nr, nc = sr + dr[ndi], sc + dc[ndi]
                    if 0 <= nr <= N - 1 and 0 <= nc <= N - 1:
                        if board[nr][nc][0] == si:
                            nxt_shark_di = ndi
                            break
            nxt_shark_loc.append((si,nr,nc))
            cur_shark_di[si] = nxt_shark_di

        # 향기 감소 / 상어 이동
        for r in range(N):
            for c in range(N):
                if board[r][c]==0:
                    continue
                elif board[r][c][1]==1:
                    board[r][c] = 0
                else:
                    board[r][c][1] -= 1

        for si, sr, sc in nxt_shark_loc:
            if board[sr][sc] == 0:
                board[sr][sc] = [si, k]
            else:
                psi, _ = board[sr][sc]
                if si <= psi:
                    board[sr][sc] = [si, k]


    return -1

print(solution())