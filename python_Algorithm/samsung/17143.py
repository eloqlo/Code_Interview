R,C,M = map(int,input().split())
sharks_dict=[[] for _ in range(C+1)]
for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    sharks_dict[c].append((r,c,s,d,z))


# 직관적이고 계층적인 풀이, 중복되는 iteration을 최대한 줄였다.
def solution(sharks_dict):
    result = 0

    #1 사람 우측 이동
    for mi in range(1,C+1):

        # 상어 먹고(t)
        # O(M)
        eat_flag = False
        min_r = 101
        min_r_z = -1
        min_idx = -1
        for idx,shark_info in enumerate(sharks_dict[mi]):
            r,c,s,d,z = shark_info
            if r < min_r:
                min_r = r
                min_r_z = z
                min_idx = idx
                eat_flag = True
        if eat_flag:
            # 그 상어 없애고, result에 질량 업데이트
            sharks_dict[mi].pop(min_idx)
            result += min_r_z

        # 상어 움직이고, 업데이트(t+1)
        # O(M)
        new_sharks_dict = [[] for _ in range(C+1)]
        checker = {}
        for sharks_per_col in sharks_dict:
            for r,c,s,d,z in sharks_per_col:
                # 새로운 포지션 구하고
                # O(C)
                nr, nc, nd = get_nxt_position_direction(r,c,s,d)
                try:    # 그자리에 상어 있으면
                    ps, pd, pz = checker[(nr,nc)]
                    if pz < z:    # 더 큰애를 저장
                        checker[(nr,nc)] = s,nd,z
                        new_sharks_dict[nc].append((nr,nc,s,nd,z))
                        new_sharks_dict[nc].remove((nr,nc,ps,pd,pz))    #TODO SC
                except:
                    checker[(nr,nc)] =  s,nd,z
                    new_sharks_dict[nc].append((nr, nc, s, nd, z))

        sharks_dict = new_sharks_dict
        del new_sharks_dict

    return result


# 이동 규칙을 정확히 찾기 (1 Hour)
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


# 디버깅 (1 Hour - speed up 요망)
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


result = solution(sharks_dict=sharks_dict)
print( result )