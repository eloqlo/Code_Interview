def p(A):
    print()
    for l in A:
        for e in l:
            print(e, end=' ')
        print()
def solution():
    R,C,K = map(int,input().split())
    new_golem_info = []
    for _ in range(K):
        c, d = map(int,input().split())
        new_golem_info.append((c-1, d))
    diff = [(-1,0),(0,1),(1,0),(0,-1)]
    A = [[0]*C for _ in range(R+3)]
    cur_gol_dict={}
    SCORE = 0

    for gol_idx in range(1, K+1):
        c, d = new_golem_info[gol_idx-1]
        for r in range(1, R+2):
            if r==R+1:
                break

            if A[r+1][c-1]+A[r+2][c]+A[r+1][c+1]==0:
                continue
            if c>=2 and A[r-1][c-1]+A[r][c-2]+A[r+1][c-1]+ A[r+1][c-2]+A[r+2][c-1]==0:
                c -= 1
                d = (d+3)%4
                continue
            if c<=C-3 and A[r-1][c+1]+A[r][c+2]+A[r+1][c+1]+ A[r+1][c+2]+A[r+2][c+1]==0:
                c += 1
                d = (d+1)%4
                continue
            break



        if r<=3:
            A = [[0] * C for _ in range(R + 3)]
            cur_gol_dict = {}
            continue

        A[r][c] = gol_idx
        for dr,dc in diff:
            nr,nc = r+dr, c+dc
            A[nr][nc] = gol_idx

        cur_gol_dict[gol_idx] = (r,c,d)
        stack = [gol_idx]
        visit = set([gol_idx])
        max_r = 0
        while stack:
            curi = stack.pop()
            cr, cc, cd = cur_gol_dict[curi]
            max_r = max(max_r, cr)
            if cr==R+1:
                break

            er,ec = cr+diff[cd][0], cc+diff[cd][1]
            for dr,dc in diff:
                nr,nc = er+dr, ec+dc
                if 0 <= nr < R+2 and 0 <= nc < C and A[nr][nc]!=0 and A[nr][nc] not in visit:
                    visit.add(A[nr][nc])
                    stack.append(A[nr][nc])
        SCORE += max_r-1
    return SCORE

print(solution())