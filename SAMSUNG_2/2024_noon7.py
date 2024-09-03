def solution():

    # INPUTS
    R,C,K = map(int, input().split())
    golems=[]
    for _ in range(K):
        c,d = map(int, input().split())
        golems.append((c-1,d))
    diff = [(-1,0),(0,1),(1,0),(0,-1)]

    A = [[0]*C for _ in range(R+3)]
    gol_info = {}
    SCORE = 0
    for gi, (gc, gd) in enumerate(golems):
        gi += 1
        for gr in range(1,R+2):
            if gr==R+1:
                break

            if A[gr+2][gc] + A[gr+1][gc-1] + A[gr+1][gc+1]==0:
                continue

            if gc>=2 and A[gr-1][gc-1]+A[gr][gc-2]+A[gr+1][gc-1]+A[gr+1][gc-2]+A[gr+2][gc-1]==0:
                gc -= 1
                gd = (gd+3)%4
                continue

            if gc<=C-3 and A[gr-1][gc+1]+A[gr][gc+2]+A[gr+1][gc+1]+A[gr+1][gc+2]+A[gr+2][gc+1]==0:
                gc += 1
                gd = (gd+1)%4
                continue
            break

        if gr <= 3:
            A = [[0] * C for _ in range(R + 3)]
            gol_info = {}
            continue

        # check in map
        A[gr][gc] = gi
        for dr,dc in diff:
            A[gr+dr][gc+dc] = gi

        gol_info[gi] = (gr,gc,gd)

        foo = [gi]
        visit = set([gi])
        MAX_R = 0
        while foo:
            curgi = foo.pop()
            curr, curc, curd = gol_info[curgi]
            MAX_R = max(curr,MAX_R)
            if MAX_R==R+1:
                break
            dr, dc = diff[curd]
            er, ec = curr+dr, curc+dc

            for dr, dc in diff:
                nr, nc = er+dr, ec+dc
                if 0<=nr<R+2 and 0<=nc<C and A[nr][nc]>0 and A[nr][nc] not in visit:
                        visit.add(A[nr][nc])
                        foo.append(A[nr][nc])

        SCORE += MAX_R-1

    return SCORE

print(solution())