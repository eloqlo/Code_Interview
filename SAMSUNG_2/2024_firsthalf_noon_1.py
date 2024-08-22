def p(A):
    for l in A:
        for e in l:
            if e==0:
                print(".",end=' ')
            else:
                print(e, end=' ')
        print()
    print()

def solution(DEBUG):
    R,C,K = map(int,input().split())
    G=[]
    for gi in range(K):
        c,d = map(int,input().split())
        G.append((gi+1,c-1,d))  # 골렘번호, 출발열, 방향
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    A = [[0]*C for _ in range(R+2)]
    cur_gol_dict = {}
    ROW_COUNTER = 0

    for gi, c, gd in G:
        # TODO SANITY CHECK
        # tmp_r,tmp_c == center
        tmp_c = c
        print("gi,dg 출격! -- ",gi,gd)
        for tmp_r in range(R+1):
            if tmp_r <= R-1:
                # down
                if A[tmp_r+2][tmp_c]==0 and A[tmp_r+1][tmp_c-1]==0 and A[tmp_r+1][tmp_c+1]==0:
                    continue
                # west
                if tmp_c > 1:
                    check = 0
                    for tr,tc in [(tmp_r+1,tmp_c-2), (tmp_r+1,tmp_c-1), (tmp_r+2,tmp_c-1)]:
                        check += A[tr][tc]
                    if not check:
                        print(f"골렘 서쪽회전, gd 변화 ({gd}->{(gd-1 + 4)%4})")
                        gd = (gd-1 + 4)%4
                        tmp_c -= 1
                        continue
                # east
                if tmp_c < C-2:
                    check = 0
                    for tr, tc in [(tmp_r + 1, tmp_c + 2), (tmp_r + 1, tmp_c + 1), (tmp_r + 2, tmp_c + 1)]:
                        check += A[tr][tc]
                    if not check:
                        print(f"골렘 동쪽회전, gd 변화 ({gd}->{(gd+1) % 4})")
                        gd = (gd+1) % 4
                        tmp_c += 1
                        continue
                break   # dead end

        if tmp_r < 3:
            A = [[0]*C for _ in range(R+2)]
            cur_gol_dict = {}
            if DEBUG:
                print("gi,c 는 착륙 못함", gi, c)
                print("****************************** pop!!")
            continue
        A[tmp_r][tmp_c] = gi
        for tmp_di in range(4):
            A[tmp_r+dr[tmp_di]][tmp_c+dc[tmp_di]] = gi
        cur_gol_dict[gi] = (tmp_r,tmp_c,gd)

        if DEBUG:
            print("________ after 착륙 / (gi,gd,c) =",gi,gd,c)
            p(A)

        # SCORING !
        stack = [gi]
        visit = set([gi])
        max_row = 0
        while stack:
            cur_gi = stack.pop()
            center_r, center_c, gd = cur_gol_dict[cur_gi]

            if center_r == R:   # TODO "bottom-1 == R" index check
                max_row = R
                break
            exit_r, exit_c = center_r+dr[gd], center_c+dc[gd]
            if not (2<=exit_r<=R+1 and 0<=exit_c<=C-1):
                raise Exception("골렘 출구 맵이탈")

            dead_end_flag = True  # 지금 위치가 마지막임
            for tmp_di in range(4):
                search_r, search_c = exit_r+dr[tmp_di], exit_c+dc[tmp_di]
                if 2<=search_r<=R+1 and 0<=search_c<=C-1:
                    if A[search_r][search_c]>0 and A[search_r][search_c] not in visit:
                        new_gi = A[search_r][search_c]
                        stack.append(new_gi)
                        visit.add(new_gi)
                        dead_end_flag = False
            if dead_end_flag:
                max_row = max(max_row, center_r+1)
        if DEBUG:
            print("score+ ",max_row)
        ROW_COUNTER += max_row
        # 1 golem end
    # for end (1 golem end)

    return ROW_COUNTER


print(solution(True))