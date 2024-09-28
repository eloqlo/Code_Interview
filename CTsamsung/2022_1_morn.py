def solution():

    # INPUTS
    N,M,H,K = map(int,input().split())
    A = [[[] for _ in range(N)] for _ in range(N)]
    runners=[]
    for ri in range(1,M+1):
        r,c,d = map(int,input().split())
        r-=1; c-=1
        runners.append([ri,r,c,d])
        A[r][c].append(ri)
    trees = set()
    for _ in range(H):
        tr,tc = map(int,input().split())
        tr-=1; tc-=1
        trees.add((tr,tc))
    dr = [0,0,1,-1]   # 좌 우(1) 하(2) 상
    dc = [-1,1,0,0]
    SCORE = 0
    sr, sc, sd = N//2, N//2, 0
    diff = [(-1,0),(0,1),(1,0),(0,-1)]  # 상 우 하 좌

    gen_get_spos = get_spos(N)
    s_order_save = [(sr,sc,sd)]
    s_reverse = False
    for t in range(1, K+1):
        moving_runners_idx = find_runners(sr,sc,A)

        # RUNNERS MOVE
        for ri in list(moving_runners_idx):
            _,rr,rc,rd = runners[ri-1]
            nr,nc = rr+dr[rd], rc+dc[rd]
            if 0<=nr<N and 0<=nc<N:
                if (nr,nc)==(sr,sc):
                    continue
            else:
                if rd==1:
                    rd=0
                elif rd==0:
                    rd=1
                elif rd==2:
                    rd=3
                else:
                    rd=2
                runners[ri-1][-1] = rd
                nr, nc = rr + dr[rd], rc + dc[rd]
                if (nr, nc) == (sr, sc):
                    continue
            runners[ri-1][1] = nr
            runners[ri-1][2] = nc
            A[rr][rc].remove(ri)
            A[nr][nc].append(ri)

        # 술레 MOVE
        sr,sc,sd = next(gen_get_spos)
        catch_count = 0
        for tmp in range(3):
            search_r, search_c = sr+diff[sd][0]*tmp, sc+diff[sd][1]*tmp
            if 0<=search_r<N and 0<=search_c<N:
                if (search_r,search_c) in trees:
                    continue
                if A[search_r][search_c]:
                    for runner_idx in A[search_r][search_c]:
                        runners[runner_idx-1][1] = None
                        runners[runner_idx-1][2] = None
                        A[search_r][search_c] = []
                        catch_count += 1
        SCORE += t*catch_count
    print(SCORE)

def get_spos(N):
    diff = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상 우 하 좌
    sr, sc, sd = N//2, N//2, 0
    repeat = 0
    backup_loc = [(sr, sc)]
    backup_di = [sd]
    end_flag = False
    rev = False
    while True:
        if not rev:
            repeat += 1
            for _ in range(2):
                for r_idx in range(repeat):
                    if (sr,sc)==(0,0):
                        end_flag = True
                        rev = True
                        break
                    sr, sc = sr + diff[sd][0], sc + diff[sd][1]
                    if r_idx == repeat - 1:
                        sd = (sd + 1) % 4
                    backup_loc.append((sr, sc))
                    backup_di.append(sd)
                    if (sr,sc) == (0,0):
                        sd = 2
                    yield sr, sc, sd
                if end_flag:
                    backup_loc.pop()
                    backup_di.pop()
                    backup_di.pop()
                    backup_loc.reverse()
                    backup_di.reverse()
                    backup_di.append(2)
                    end_flag = False
                    break
        else:
            for (sr,sc),sd in zip(backup_loc, backup_di):
                sd = (sd+2)%4
                yield sr,sc,sd
            rev = False
            backup_loc = [(sr, sc)]
            backup_di = [sd]
            repeat = 0

def find_runners(sr,sc,A):
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    found_runners = set()
    length = 3
    N = len(A)
    dq = [(sr,sc)]
    visit = set([(sr,sc)])
    for _ in range(length):
        nxt_dq=[]
        while dq:
            cr,cc = dq.pop()
            for di in range(4):
                nr,nc = cr+dr[di], cc+dc[di]
                if 0<=nr<N and 0<=nc<N and (nr,nc) not in visit:

                    nxt_dq.append((nr,nc))
                    visit.add((nr,nc))
                    if A[nr][nc]:
                        for ele in A[nr][nc]:
                            found_runners.add(ele)
        dq = nxt_dq
    return found_runners


def p(A,sr,sc):
    for r,l in enumerate(A):
        for c,e in enumerate(l):
            if (r,c)==(sr,sc):
                print('S', end=' ')
            elif e!=0:
                print(e, end=' ')
            else:
                print(".", end=' ')
        print()

solution()