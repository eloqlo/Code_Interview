def get_dist(r1,c1,r2,c2):
    return (r1-r2)**2 + (c1-c2)**2

def get_nxt_rud_loc(A, santa, rudr, rudc):

    diff = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    N = len(A)

    min_dist = 1e6
    minr, minc = 0, 0
    santa_sorted = sorted(list(santa.values()), key = lambda x:(-x[0],-x[1]))
    for sr, sc in santa_sorted:
        distance = get_dist(rudr,rudc,sr,sc)
        if distance < min_dist:
            min_dist = distance
            minr, minc = sr, sc
    min_dist = 1e6
    nxt_rudr, nxt_rudc = None, None
    nxt_dr, nxt_dc = None, None
    for dr,dc in diff:
        nr, nc = rudr+dr, rudc+dc
        if 0 <= nr < N and 0 <= nc < N:
            cur_dist = get_dist(minr,minc,nr,nc)
            if cur_dist < min_dist:
                min_dist = cur_dist
                nxt_rudr, nxt_rudc = nr, nc
                nxt_dr, nxt_dc = dr, dc

    if nxt_rudr==None:
        raise Exception("cur rud can't make next move.")

    return nxt_rudr, nxt_rudc, nxt_dr, nxt_dc

def get_nxt_san_loc(A, sr, sc, rudr, rudc):

    diff = [(-1,0), (0,1), (1,0), (0,-1)]
    N = len(A)

    min_dist = 1e6
    cur_dist = get_dist(sr,sc,rudr,rudc)
    nxtr, nxtc = None, None
    mindr, mindc = None, None
    for dr, dc in diff:
        nr, nc = sr+dr, sc+dc
        if 0 <= nr < N and 0 <= nc < N and A[nr][nc] <= 0:
            new_dist = get_dist(nr,nc,rudr,rudc)
            if new_dist < cur_dist and new_dist < min_dist:
                min_dist = new_dist
                nxtr, nxtc = nr, nc
                mindr, mindc = dr, dc

    return nxtr, nxtc, mindr, mindc

def solution():

    # INPUTS
    N, M, P, C, D = map(int,input().split())
    A = [[0]*N for _ in range(N)]
    rudr, rudc = map(int,input().split())
    rudr -= 1; rudc -= 1
    A[rudr][rudc] = -1
    santa = {}
    for _ in range(1, P+1):
        si, sr, sc = map(int,input().split())
        sr-=1; sc-=1
        santa[si] = (sr,sc)
        A[sr][sc] = si
    santa_score = [0]*(P+1)
    stun_san_old = set()

    for turn_m in range(M):

        stun_san_new = set()
        nxt_rudr, nxt_rudc, nxt_dr, nxt_dc = get_nxt_rud_loc(A, santa, rudr, rudc)

        # RUD MOVE
        if (nxt_rudr, nxt_rudc) in santa.values():
            A[rudr][rudc] = 0
            hit_si = A[nxt_rudr][nxt_rudc]
            rudr, rudc = nxt_rudr, nxt_rudc
            A[rudr][rudc] = -1

            # MOVE HIT SANTA
            stun_san_new.add(hit_si)
            santa_score[hit_si] += C
            nxt_sr, nxt_sc = rudr + nxt_dr*C, rudc + nxt_dc*C
            nxt_santa = [(nxt_sr, nxt_sc, hit_si)]
            while nxt_santa:
                nxt_sr, nxt_sc, hit_si = nxt_santa.pop()
                if not (0 <= nxt_sr < N and 0 <= nxt_sc < N):
                    santa.pop(hit_si)
                    break
                nxt_si = A[nxt_sr][nxt_sc]
                A[nxt_sr][nxt_sc] = hit_si
                santa[hit_si] = (nxt_sr, nxt_sc)
                if nxt_si>0:
                    nxt_santa.append([nxt_sr+nxt_dr, nxt_sc+nxt_dc, nxt_si])
        else:
            A[rudr][rudc] = 0
            rudr, rudc = nxt_rudr, nxt_rudc
            A[rudr][rudc] = -1

        # SANTA MOVE
        for si in sorted(list(santa.keys())):
            if si not in santa or si in stun_san_new or si in stun_san_old:
                continue
            sr, sc = santa[si]
            nxt_sr, nxt_sc, nxt_san_dr, nxt_san_dc = get_nxt_san_loc(A, sr, sc, rudr, rudc)

            if nxt_sr == None:
                continue

            A[sr][sc] = 0

            if A[nxt_sr][nxt_sc] == 0:
                A[nxt_sr][nxt_sc] = si
                santa[si] = (nxt_sr, nxt_sc)
            elif A[nxt_sr][nxt_sc]>0:
                raise Exception()
            else:
                # si meet rud
                santa_score[si] += D
                stun_san_new.add(si)
                nxt_sr, nxt_sc = nxt_sr - nxt_san_dr*D, nxt_sc - nxt_san_dc*D

                nxt_santa = [(nxt_sr, nxt_sc, si)]
                while nxt_santa:
                    nxt_sr, nxt_sc, hit_si = nxt_santa.pop()
                    if not (0 <= nxt_sr < N and 0 <= nxt_sc < N):
                        santa.pop(hit_si)
                        break
                    nxt_si = A[nxt_sr][nxt_sc]
                    A[nxt_sr][nxt_sc] = hit_si
                    santa[hit_si] = (nxt_sr, nxt_sc)
                    if nxt_si > 0:
                        nxt_santa.append([nxt_sr - nxt_san_dr, nxt_sc - nxt_san_dc, nxt_si])
        for key in santa.keys():
            santa_score[key] += 1
        stun_san_old = stun_san_new
    for s in santa_score[1:]:
        print(s, end=' ')
    return

solution()