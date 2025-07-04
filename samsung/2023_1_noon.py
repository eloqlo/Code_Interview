def p(A):
    print()
    for l in A:
        for e in l:
            print(e, end='\t')
        print()

def solution():

    N,M,K = map(int, input().split())
    A=[]
    for _ in range(N):
        A.append(list(map(int,input().split())))
    runners=[]
    for _ in range(M):
        r,c = map(int,input().split())
        runners.append((r-1,c-1))
    er, ec = map(int, input().split())
    er-=1; ec-=1
    diff = [(-1,0),(1,0),(0,-1),(0,1)]  # 상 하 좌 우
    TOTAL_DIST = 0


    for turn_k in range(K):

        # RUNNERS MOVE
        CUR_DIST_COUNT = 0
        new_runners = []
        for rr, rc in runners:
            # 특정 runner
            start_dist = abs(rr-er) + abs(rc-ec)    # 처음 ~ 출구
            min_dist = 1e6
            nxtr, nxtc = None, None
            for dr,dc in diff:
                nr,nc = rr+dr, rc+dc
                if 0<=nr<N and 0<=nc<N and A[nr][nc]==0:
                    comp_dist = abs(nr-er) + abs(nc-ec)
                    if comp_dist < start_dist and comp_dist < min_dist:
                        min_dist = comp_dist
                        nxtr, nxtc = nr, nc
            if nxtr != None:
                CUR_DIST_COUNT += 1
                if not (er,ec) == (nxtr,nxtc):
                    new_runners.append((nxtr,nxtc))
            else:
                new_runners.append((rr, rc))
        runners = new_runners
        TOTAL_DIST += CUR_DIST_COUNT

        # print("AFTER MOVE")
        # print("MOVED/TOTAL ",CUR_DIST_COUNT,'/ ',TOTAL_DIST)

        if len(runners)==0:
            break


        # find square
        tmp_squares = []  # length, left_high_r, left_high_c
        for rr,rc in runners:
            side = max(abs(rr-er)+1, abs(rc-ec)+1)

            bottom_r = max(rr,er)
            right_c = max(rc,ec)

            lhr = max(0, bottom_r - (side-1))
            lhc = max(0, right_c - (side-1))

            tmp_squares.append((side, lhr, lhc))
        tmp_squares.sort(key = lambda x:(x[0], x[1], x[2]))

        side, lhr, lhc = tmp_squares[0]
        # print("left high r,c ", lhr, lhc, "/ side len ",side)

        A_tmp = [line.copy() for line in A]
        A_tmp[er][ec] = "E"
        for idx, (rr,rc) in enumerate(runners):
            if A_tmp[rr][rc] == 0:
                A_tmp[rr][rc] = [idx]
            else:
                A_tmp[rr][rc].append(idx)
        bf_rotate = [A_tmp[row][lhc:lhc+side] for row in range(lhr,lhr+side)]
        af_rotate = list(zip(*bf_rotate[::-1]))

        for r, new_line in enumerate(af_rotate):
            for c, ele in enumerate(new_line):
                new_r = r + lhr
                new_c = c + lhc
                if ele == 0:
                    A[new_r][new_c] = 0
                    continue
                elif type(ele) == int and ele > 0:
                    A[new_r][new_c] = ele - 1
                elif ele == 'E':
                    er, ec = new_r, new_c
                    A[new_r][new_c] = 0
                else:
                    A[new_r][new_c] = 0
                    for runner_idx in ele:
                        runners[runner_idx] = (new_r, new_c)

        # p(A)
        # print("_______________",turn_k," turn end ________________")


    return (TOTAL_DIST, er+1, ec+1)

dist, er, ec = solution()
print(dist)
print(er, ec)