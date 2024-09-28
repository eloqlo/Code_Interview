def solution():

    R,C,K = map(int, input().split())
    gol_info=[]
    idx = 1
    for _ in range(K):
        c,d = map(int, input().split())
        gol_info.append((c-1, d, idx))
        idx+=1
    diff = [(-1,0),(0,1),(1,0),(0,-1)]  # 북 동 남 서
    A = [[0]*C for _ in range(R+3)]
    gol_dict = {}
    SCORE = 0

    for curc, curd, golidx in gol_info:
        for curr in range(1,R+2):

            if curr == R+1:
                break
            if A[curr+2][curc] + A[curr+1][curc-1] + A[curr+1][curc+1] == 0:
                continue
            if curc >= 2 and A[curr-1][curc-1] + A[curr][curc-2] + A[curr+1][curc-1] + A[curr+1][curc-2] + A[curr+2][curc-1]==0:
                curc-=1
                curd = (curd+3)%4
                continue
            if curc <= C-3 and A[curr-1][curc+1] + A[curr][curc+2] + A[curr+1][curc+1] + A[curr+1][curc+2] + A[curr+2][curc+1]==0:
                curc+=1
                curd = (curd+1)%4
                continue
            break

        # check
        if curr<=3:
            A = [[0] * C for _ in range(R + 3)]
            gol_dict = {}
            continue

        # insert
        if A[curr][curc] >0:
            raise Exception()
        A[curr][curc] = golidx
        for dr,dc in diff:
            if A[curr+dr][curc+dc]>0:
                raise Exception(A[curr+dr][curc+dc])
            A[curr+dr][curc+dc] = golidx
        gol_dict[golidx] = (curr,curc,curd)

        # escape
        dq = [golidx]
        visit = set([A[curr][curc]])
        max_row = 0
        while dq:
            gi = dq.pop()
            cr,cc,cd = gol_dict[gi]
            er,ec = cr+diff[cd][0], cc+diff[cd][1]
            if max_row < cr:
                max_row = cr
                if max_row==R+1:
                    break
            for dr,dc in diff:
                nr,nc = er+dr, ec+dc
                if 0<=nr<=R+2 and 0<=nc<C and A[nr][nc]>0 and A[nr][nc] not in visit:
                    tmp = A[nr][nc]
                    visit.add(tmp)
                    dq.append(tmp)
        # p(A)
        SCORE += max_row-1
    print(SCORE)

def p(A):
    for l in A:
        for e in l:
            if e==0:
                print('.',end=' ')
            else:
                print(e,end=' ')
        print()
    print()
solution()