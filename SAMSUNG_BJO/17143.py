R,C,M = map(int,input().split())
sharks_arr=[]
for _ in range(M):
    sharks_arr.append(list(map(int, input().split())))

def solution(debug):
    global sharks_arr
    result = 0
    dead_sharks = []
    
    for man_col_idx in range(1,C+1):

        # debug: print board before man catch shark
        if debug:
            board_print = [['#'] * (C + 2)]
            board_print += [["#"] + ['.']*C + ["#"] for _ in range(R)]
            board_print.append(['#'] * (C + 2))
            for r,c,s,d,z in sharks_arr:
                if r==-1:
                    continue
                board_print[r][c] = z
            print(f"__________________at: {man_col_idx}____________________")
            for line in board_print:
                for ele in line:
                    print(ele, end=' ')
                print()

        #1 make inital board
        board = [[(-1,-1)]*(C+2) for _ in range(R+2)]

        for si in range(len(sharks_arr)):
            if si not in dead_sharks:
                r, c, s, d, z = sharks_arr[si]
                board[r][c] = (si, z)

        #2 catch shark if man can.
        for board_row_idx in range(1, R + 1):
            if board[board_row_idx][man_col_idx][1] >= 1:
                si, z = board[board_row_idx][man_col_idx]
                dead_sharks.append(si)
                result += z
                break

        #3 update sharks position
        tmp_sharks_arr = []
        board = [[(-1, -1)] * (C + 2) for _ in range(R + 2)]
        for si in range(len(sharks_arr)):
            r, c, s, d, z = sharks_arr[si]
            # except dead sharks
            if si in dead_sharks:
                tmp_sharks_arr.append([-1,-1,-1,-1,-1])
                continue
            
            #get next position, direction
            nr, nc, nd = get_nxt_position_direction(r,c,s,d)
            tmp_sharks_arr.append((nr,nc,s,nd,z))
            
            # 이동한 위치 기반으로 죽은 상어 솎아내기
            _si, _z = board[nr][nc]
            if _si == -1:
                board[nr][nc] = (si, z)
            else:
                if _z < z:
                    board[nr][nc] = (si, z)
                    dead_sharks.append(_si)
                else:
                    dead_sharks.append(si)
        sharks_arr = tmp_sharks_arr
    
    return result


def position_overflow_minus(ni, N):
    val = (-ni)%(N-1)
    if ((-ni)//(N-1))%2 == 0:
        is_flip=True
        ni = val+2
    else:
        is_flip=False
        ni = N-1 - val
    return ni, is_flip

def position_overflow_plus(ni, N):
    val = ni - (N+1)
    if (val//(N-1)) % 2 == 0:
        is_flip=True
        ni = N-1 - (val%(N-1))
    else:
        is_flip = False
        ni = 2 + val%(N-1)
    return ni, is_flip

def get_nxt_position_direction(r,c,s,d):
    global R,C
    if d==1:    # 위
        nr = r - s
        nc = c
        nd = d
        if nr<1:
            nr, is_flip = position_overflow_minus(nr, R)
            if is_flip:
                nd = 2

    elif d==4:  # 왼쪽
        nr = r
        nc = c - s
        nd = d
        if nc<1:
            nc, is_flip = position_overflow_minus(nc, C)
            if is_flip:
                nd = 3

    elif d==2:  # 아래
        nr = r + s
        nc = c
        nd = d
        if nr>R:
            nr,is_flip = position_overflow_plus(nr, R)
            if is_flip:
                nd = 1

    elif d==3:  # 오른쪽
        nr = r
        nc = c + s
        nd = d
        if nc>C:
            nc,is_flip = position_overflow_plus(nc, C)
            if is_flip:
                nd = 4
    else:
        raise

    return nr, nc, nd


def debug_nxt_pos(nR,nC, r,c,s, d):
    global  R, C
    R = nR
    C = nC
    board = [["#"]*(C+2)]
    board += [["#"]+['.']*C+["#"] for _ in range(R)]
    board.append(["#"]*(C+2))
    board[r][c] = 'S'
    nr,nc,nd = get_nxt_position_direction(r,c,s,d)
    print("nr,nc: ", nr,nc)
    print("speed: ", s)
    print("d,nd: ",d,nd, end=' ')
    if d==1:
        print('위')
    elif d==2:
        print('아래')
    elif d==3:
        print('오른쪽')
    elif d==4:
        print('왼쪽')

    print("________og board_________")
    for line in board:
        for ele in line:
            print(ele, end=' ')
        print()

    print("_______after board________")
    board[nr][nc] = "N"
    for line in board:
        for ele in line:
            print(ele, end=' ')
        print()


if __name__ == "__main__":
    result = solution(debug=False)
    print( result )

    # debug_nxt_pos(4,5, 2,2,14, 1)