def p(A):
    for l in A:
        for e in l:
            print(e, end=' ')
        print()
    print()

def solution():
    R,C,K = map(int,input().split())
    G=[None]
    for _ in range(K):
        c,d=map(int,input().split())
        G.append((c-1,d))
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    A=[[0]*C for _ in range(R+3)]
    golems={}
    score = 0

    for gi in range(1,K+1):

        c,di = G[gi]

        for r in range(1,R+2):
            if r==R+1:
                break
            # down
            nr = r+1
            nc = c
            if A[nr][nc-1]==0 and A[nr+1][nc]==0 and A[nr][nc+1]==0:
                continue
            # left
            if c>=2:
                nr = r
                nc = c-1
                if A[nr][nc-1]==0 and A[nr-1][nc]==0 and A[nr+1][nc]==0:
                    if A[nr+2][nc]==0 and A[nr+1][nc-1]==0:
                        c-=1
                        di = (di-1+4)%4
                        continue
            # right
            if c<=C-3:
                nr, nc = r, c+1
                if A[nr][nc+1]==0 and A[nr-1][nc]==0 and A[nr+1][nc]==0:
                    if A[nr+2][nc]==0 and A[nr+1][nc+1]==0:
                        c+=1
                        di = (di+1) % 4
                        continue
            break
        if r <= 3:
            A = [[0] * C for _ in range(R + 3)]
            golems={}
            continue

        if A[r][c] != 0:
            print("Exception: ",A[r][c])
            raise Exception
        A[r][c] = gi
        for tmp_di in range(4):
            nr,nc = r+dr[tmp_di], c+dc[tmp_di]
            if A[nr][nc]!=0:
                print(f"{nr,nc} 위치({A[nr][nc]})에 {gi}넣으려 함")
                p(A)
                raise Exception
            A[nr][nc] = gi
        golems[gi] = (r,c,di)


        visit=[gi]
        stack=[gi]
        lowest_point = 0
        while stack:
            cur_gi = stack.pop()
            tmpr, tmpc, tmpdi = golems[cur_gi]
            lowest_point = max(tmpr, lowest_point)
            if tmpr==R+1:   #TODO sanity check
                lowest_point = R+1
                break
            er,ec = tmpr+dr[tmpdi], tmpc+dc[tmpdi]
            for foo in range(4):
                nr,nc = er+dr[foo], ec+dc[foo]
                if 0<=nr<R+3 and 0<=nc<C:
                    new_gi = A[nr][nc]
                    if new_gi != 0 and new_gi not in visit:
                        stack.append(new_gi)
                        visit.append(new_gi)
        score += lowest_point-1

    return score

print(solution())