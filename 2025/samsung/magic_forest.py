from collections import deque

def pf(f):
    for line in f:
        for e in line:
            print(e,end=' ')
        print()
    print("_____________")


def solution():
    R,C,K = map(int,input().split())

    angel_arr = []
    for ai in range(K):
        c,d = map(int,input().split())
        c -= 1  # normalize
        angel_arr.append([ai+1,c,d])

    #TODO F sanity check
    F = [[0 for _ in range(C)] for _ in range(R+3)]   

    #TODO dr,dc sanity check
    dr = [-1,0,1,0]     # 북 동 남 서
    dc = [0,1,0,-1]

    SCORE = 0
    ai_dict = {}
    for ai, ci, di in angel_arr:
        ai += 1
        # GOING DOWN
        for ri in range(1,R+2):
            # Reach BOTTOM
            if ri==R+1:
                break
            
            # VERTICAL / LEFT / RIGHT
            if F[ri+2][ci] + F[ri+1][ci-1] + F[ri+1][ci+1] == 0:
                continue
            elif ci >= 2 and (F[ri-1][ci-1] + F[ri][ci-2] + F[ri+1][ci-2] + F[ri+1][ci-1] + F[ri+2][ci-1])==0:
                ci -= 1
                di = (di+3)%4      
                continue
            elif ci <= C-3 and (F[ri-1][ci+1] + F[ri][ci+2] + F[ri+1][ci+1] + F[ri+2][ci+1] + F[ri+1][ci+2])==0:
                ci += 1
                di = (di+1)%4      
                continue
            break

        # OVERFLOW -> RESET
        if ri <= 3:
            F = [[0 for _ in range(C)] for _ in range(R+3)]
            ai_dict = {}
            continue

        # Sanity Check / F update / di_arr update
        for idx in range(4):
            tst_r, tst_c = ri + dr[idx], ci + dc[idx]
            if F[tst_r][tst_c]:
                raise Exception("After Down, ERR in location")
            F[tst_r][tst_c] = ai
        F[ri][ci] = ai
        ai_dict[ai] = [ri,ci,di]

        # ANGEL MOVE
        # GO LOW -> Brute Force + BFS
        visit = set()
        visit.add(ai)
        nxt_loc = deque([ai])
        DEEPEST_R = ri+1
        while nxt_loc:
            cur_ai = nxt_loc.popleft()
            cur_r, cur_c, cur_d = ai_dict[cur_ai]
            if cur_r+1 > DEEPEST_R:
                DEEPEST_R = cur_r+1
            if DEEPEST_R == R+2:
                break

            # Search
            er, ec = cur_r + dr[cur_d], cur_c + dc[cur_d]
            for idx2 in range(4):
                nr, nc = er+dr[idx2], ec+dc[idx2]
                if 0<=nr<=R+2 and 0<=nc<=C-1 and F[nr][nc] > 0 and F[nr][nc] not in visit:
                    nxt_loc.append(F[nr][nc])
                    visit.add(F[nr][nc])
        SCORE += DEEPEST_R - 2
    return SCORE


if __name__ == "__main__":

    result = solution()
    print(result)