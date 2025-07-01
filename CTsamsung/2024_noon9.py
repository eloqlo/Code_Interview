def solution():
    R,C,K = map(int,input().split())
    gols=[]
    gi=1
    for _ in range(K):
        c,d = map(int,input().split())
        gols.append((gi,c-1,d))
        gi+=1
    diff = [(-1,0),(0,1),(1,0),(0,-1)]
    A = [[0]*C for _ in range(R+3)]
    gol_dict = {}
    SCORE = 0

    for gi,gc,gd in gols:
        for gr in range(1,R+2):

            if gr==R+1:
                break
            if A[gr+2][gc] + A[gr+1][gc-1] + A[gr+1][gc+1] == 0:
                continue
            if gc>=2 and A[gr-1][gc-1]+A[gr][gc-2]+A[gr+1][gc-1] + A[gr+1][gc-2]+A[gr+2][gc-1]==0:
                gc -= 1
                gd = (gd+3)%4
                continue
            if gc<=C-3 and A[gr-1][gc+1]+A[gr][gc+2]+A[gr+1][gc+1] + A[gr+1][gc+2]+A[gr+2][gc+1]==0:
                gc += 1
                gd = (gd+1)%4
                continue
            break

        if gr<=3:
            A = [[0] * C for _ in range(R + 3)]
            gol_dict = {}
            continue

        A[gr][gc] = gi
        for dr,dc in diff:
            nr,nc = gr+dr, gc+dc
            A[nr][nc] = gi
        gol_dict[gi] = (gr,gc,gd)

        dq = [gi]
        visit = set([gi])
        max_row = 0
        while dq:
            curgi = dq.pop()
            cr,cc,cd = gol_dict[curgi]
            max_row = max(cr, max_row)
            if max_row==R+1:
                break

            er,ec = cr+diff[cd][0], cc+diff[cd][1]
            for dr,dc in diff:
                nr,nc = er+dr, ec+dc
                if 0<=nr<R+3 and 0<=nc<C and A[nr][nc]>0 and A[nr][nc] not in visit:
                    visit.add(A[nr][nc])
                    dq.append(A[nr][nc])

        SCORE += max_row-1

    print(SCORE)


solution()