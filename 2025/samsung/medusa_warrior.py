from collections import deque

def pM(M):
    for l in M:
        for e in l:
            print(e, end=' ')
        print()
    print("____________")

#* SANITY CHECK PASS
def shorest_dist(mr,mc,tr,tc,M_og):

    N = len(M_og)
    dr = [-1,1,0,0]     # 상 하 좌 우 //우선순위
    dc = [0,0,-1,1]
    MIN_DIRC = -1       # 최소 거리의 방향
    MIN_DIST = 1e9      # 현재 최소 거리

    for di in range(4):
        M = [line.copy() for line in M_og]
        M[mr][mc] = 1
        nr,nc = mr+dr[di], mc+dc[di]
        if (not 0<=nr<=N-1) or (not 0<=nc<=N-1) or M[nr][nc]==1:
            continue
        M[nr][nc] = 2
        cur = deque()
        cur.append([nr,nc])
        CUR_DIST = 2
        END_FLAG = False
        while cur:
            nxt = deque()
            CUR_DIST += 1
            # Search in this LEVEL!
            for r1, c1 in cur:
                for tmp_di in range(4):
                    r2, c2 = r1 + dr[tmp_di], c1 + dc[tmp_di]
                    if 0<=r2<=N-1 and 0<=c2<=N-1 and M[r2][c2]==0:
                        M[r2][c2] = CUR_DIST    # visit
                        nxt.append([r2,c2])     # nxt 큐에 추가
                        if r2==tr and c2==tc:
                            END_FLAG = True
                            if CUR_DIST < MIN_DIST:
                                MIN_DIRC = di
                            break
                if END_FLAG:
                    break
            if END_FLAG:
                break
            cur = nxt
        
    return MIN_DIRC # -1|Stuck, 0~3|direction

def killer_move(W:dict, mr:int, mc:int, N:int) -> dict:
    """
    >>> param
    W       dict    전사idx:[x,y]
    N       map size
    mr      int 
    mc      int

    >>> 내부
    1. 메두사 방향별 돌되는 Warrior 인덱스 찾기
    2. 돌 안된 Warrior들 메두사로 최단거리 전진 규칙1, 규칙2
        -> 돌 된 애들 명수 계산
        -> 전진거리 합 계산
        -> 메두사 닿는 애들 rm, 명수 계산
    3. 3가지 계산값 print
    4. 죽고 변경된 Warrior위치 dict 반환
    """
    def _deep_copy(M):
        new_M = []
        for line in M:
            new_line = []
            for li in line:
                new_line.append(li.copy())
            new_M.append(new_line)
        return new_M
    
    def _rot_180(_M):           # 180회전
        return [line[::-1] for line in _deep_copy(_M)[::-1]]
    def _rot_rev_90(_M):        # 반시계
        M = _deep_copy(_M)
        return list(map(list,zip(*M)))[::-1]
    def _rot_90(_M):       # 시계
        M = [line[::-1] for line in _deep_copy(_M)]
        M = list(map(list,zip(*M)))
        return M

    M = [[[] for _ in range(N)] for _ in range(N)]
    for wi in W.keys():
        r,c = W[wi]
        M[r][c].append(wi)
    M[mr][mc].append(-1)
    dr1 = [-1,1,0,0]
    dc1 = [0,0,-1,1]
    dr2 = [0,0,-1,1]
    dc2 = [-1,1,0,0]
    
    # 상하좌우 순서로 최다 돌되는 경우를 찾는다.
    STONE_COUNT = 0
    final_stone_wi = set()
    for di in range(4):
        if di==0:
            _M = _rot_180(M)
            _mr, _mc = N-mr, N-mc
        elif di==1:
            _M = _deep_copy(M)
            _mr, _mc = mr, mc
        elif di==2:
            _M = _rot_rev_90(M)
            _mr, _mc = N-mc, mr
        else:
            _M = _rot_90(M)
            _mr, _mc = mc, N-mr

        # 메두사의 시선에 따른 모든 병사들을 stone_w_queue에 저장한다.
        stone_w_queue = deque()
        in_area_wi = []
        for row_coef in range(1,N):
            newr, newc = _mr + row_coef, _mc
            if newr >= N:
                break
            if _M[newr][newc]:
                stone_w_queue.append((0, [newr,newc], _M[newr][newc]))      # down, loc, wi
                in_area_wi += _M[newr][newc]

            for col_coef in range(0,row_coef+1):
                newr, newc = _mr + row_coef, _mc + col_coef
                if 0<=newr<=N-1 and 0<=newc<=N-1 and _M[newr][newc]:
                    stone_w_queue.append((1, [newr,newc], _M[newr][newc]))      # 하우, loc, wi
                    in_area_wi += _M[newr][newc]
                newr, newc = _mr + row_coef, _mc - col_coef
                if 0<=newr<=N-1 and 0<=newc<=N-1 and _M[newr][newc]:
                    stone_w_queue.append((-1, [newr,newc], _M[newr][newc]))      # 하좌좌, loc, wi
                    in_area_wi += _M[newr][newc]

        #TODO - Sanity Check
        # stone_w_queue중 가려지는 병사들의 index를 추린다
        shadow_wi = set()       # 가려지는 병사들
        for w_di,[w_r, w_c], w_wi in stone_w_queue:     # 메두사 범위 내 병사들.
            for foo in w_wi:    
                if foo in shadow_wi:
                    continue_flag=True
                    break
            if continue_flag:
                continue
            
            for foo in range(1,N):
                if w_r + foo == N:
                    break
                for bar in range(1, foo+1):
                    if (w_c + w_di*bar) < 0 or (w_c + w_di*bar) > N-1:
                        break
                    if _M[w_r + foo][w_c + w_di*bar]:
                        for bar in _M[w_r+foo][w_c]:
                            shadow_wi.add(bar)

        in_area_wi = set(in_area_wi)
        stone_wi = set()
        for foo in in_area_wi:
            if foo not in shadow_wi:
                stone_wi.add(foo)
        if len(stone_wi) > STONE_COUNT:
            STONE_COUNT = len(stone_wi)
            final_stone_wi = stone_wi
    # 최대로 돌이되는 경우의 병사들 인덱스를 구함.



    # 움직일 wi를 추리고, W의 병사들에 대해 전진한다.
    #! 전진거리 합 계산
    DEAD_COUNT = 0
    MOVE_COUNT = 0
    visit_wi = set()
    for mov_wi in W.keys():
        if mov_wi in stone_wi or mov_wi in visit_wi:
            continue
        
        mov_r, mov_c = W[mov_wi] 
        for foo in M[mov_r][mov_c]:
            visit_wi.add(foo)
        
        min_dist = 1e9
        final_di = None
        for di in range(4):
            new_r, new_c = mov_r + dr1[di], mov_c + dc1[di]
            if 0 <= new_r <= N-1  and  0 <= new_c <= N-1:
                new_dist = abs(mr - new_r) + abs(mc - new_c)
                if new_dist < min_dist:
                    final_di = di
        


    # 한번 더 전진한다.

    # 돌 된 애들 수, 전진거리 합, 닿은애들 명수 출력

    # 죽은애들 반영 + 새로워진 전자 위치 -> W 반환


    

def solution():
    # INPUTS
    N,M = map(int, input().split())
    sr,sc,er,ec = map(int, input().split())
    mr,mc = sr,sc
    W = {}
    _w_list = list(map(int, input().split()))
    for wi in range(M):
        W[wi+1] = _w_list[wi*2:wi*2+2]
    M = [list(map(int,input().split())) for _ in range(N)]
    dr = [-1,1,0,0]     # 상 하 좌 우 //우선순위
    dc = [0,0,-1,1]


    """ ALGORITHM
    1. 공원까지 최단 방향 구하기
    2. 메두사 이동
    3. 전사들 전진

    Should be less than -> O(4M)
    """
    while True:
        short_di = shorest_dist(mr,mc,er,ec,N)
        if short_di == -1:
            print(-1)
            return
        mr, mc = mr + dr[short_di], mc + dc[short_di]
        if (mr,mc) == (er,ec):
            print(0)
            return
        W = killer_move(W,mr,mc,M)




if __name__=="__main__":
    solution()