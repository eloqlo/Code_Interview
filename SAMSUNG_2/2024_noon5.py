def solution():
    R,C,K = map(int, input().split())
    G=[]
    for _ in range(K):
        c,d = map(int, input().split())
        G.append((c-1,d))
    diff = [(-1,0),(0,1),(1,0),(0,-1)]
    A = [[0]*C for _ in range(R+3)]
    cur_golem_info = {}
    SCORE = 0

    gol_idx = 0
    for gol_c, gol_di in G:
        gol_idx += 1
        for gol_r in range(1,R+2):
            if gol_r==R+1:
                break

            if A[gol_r+2][gol_c]==0 and A[gol_r+1][gol_c-1]==0 and A[gol_r+1][gol_c+1]==0:
                continue
            if gol_c>=2 and A[gol_r-1][gol_c-1]+A[gol_r][gol_c-2]+A[gol_r+1][gol_c-1]==0 and \
                    A[gol_r+1][gol_c-2]+A[gol_r+2][gol_c-1]==0:
                gol_c-=1
                gol_di = (gol_di-1+4)%4
                continue
            if gol_c<=C-3 and A[gol_r-1][gol_c+1]+A[gol_r][gol_c+2]+A[gol_r+1][gol_c+1]==0 and \
                    A[gol_r+1][gol_c+2]+A[gol_r+2][gol_c+1]==0:
                gol_c+=1
                gol_di = (gol_di+1)%4
                continue
            break

        if gol_r <= 3:
            A = [[0] * C for _ in range(R + 3)]
            cur_golem_info = {}
            continue

        if A[gol_r][gol_c] != 0:
            raise Exception()
        A[gol_r][gol_c] = gol_idx
        for dr,dc in diff:
            A[gol_r+dr][gol_c+dc] = gol_idx
        cur_golem_info[gol_idx] = (gol_r, gol_c, gol_di)

        dq = [gol_idx]
        visit = set([gol_idx])
        max_row = 0
        while dq:
            cur_idx = dq.pop()
            cur_r, cur_c, cur_di = cur_golem_info[cur_idx]
            er, ec = cur_r+diff[cur_di][0], cur_c+diff[cur_di][1]

            if cur_r > max_row:
                max_row = cur_r
            if max_row == R+1:
                break

            for dr,dc in diff:
                nr, nc = er+dr, ec+dc
                if 0<=nr<R+2 and 0<=nc<C and A[nr][nc]>0 and A[nr][nc] not in visit:
                    dq.append(A[nr][nc])
                    visit.add(A[nr][nc])
        SCORE += max_row-1

    return SCORE

print(solution())