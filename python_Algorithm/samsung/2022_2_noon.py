def solution(DEBUG):

    # INPUTS
    N,M = map(int,input().split())
    A = []
    for _ in range(N):
        line = list(map(int,input().split()))
        A.append(line)
    store = {}
    for si in range(1,M+1):
        x,y = map(int,input().split())
        store[si] = (x-1,y-1)
        A[x-1][y-1] = 2

    """
    [1턴]
    
    1. 격자 내 사람들이 편의점 최단거리 방향으로 1칸 이동
        - (r,c)의 사람i 에 대해, 편의점i 까지 최단거리
            * BFS(hr,hc,gr,gc,A) -> 최단거리
            * 상하좌우 인접한 칸 중 도달하기까지 가야하는 칸 수가 최소가 되는 칸
            * 무조건 갈 수 있는 칸이 있다! (모든 사람은 편의점에 도착 가능함. 갇힐일 X)
    2. 도착 시 편의점에서 멈추고, 다음턴부터 그 칸을 지날 수 없게됨
        - 제외된 편의점과 베이스캠프 기록하는 visit
    3. t(<=M)번 사람이 편의점 근처 베이스캠프에 들어가 출발준비함, 그 칸은 영구적으로 X.
        - 베이스캠프 근처 편의점 store_index reutrn   
            * BFS_store(br,bc,A) -> 우선순위 고려 근처 편의점
    
    - 턴이 끝나면 사람을 pop해주고, 사람이 없으면 종료.
    """
    humans = []
    now_time = 0
    while True:
        now_time +=1
        nxt_humans = []

        if DEBUG:
            print(f"______ {now_time} min, START !!! _______")
            pm(A,humans)
            input()

        #1 - 사람들 편의점 최단거리 이동
        while humans:
            hi,hr,hc = humans.pop()
            gr,gc = store[hi]
            nxt_hr, nxt_hc = get_nxt_loc(hr,hc,gr,gc,A)
            nxt_humans.append((hi,nxt_hr,nxt_hc))

        if DEBUG:
            print(f"AFTER HUMANS MOVE")
            pm(A,nxt_humans)
            input()

        #2 도착한 사람 문 닫기
        humans = []
        for hi, nxt_hr, nxt_hc in nxt_humans:
            gr,gc = store[hi]
            if (gr,gc) == (nxt_hr, nxt_hc):
                A[gr][gc] = -1
            else:
                humans.append((hi, nxt_hr, nxt_hc))

        if DEBUG:
            print("AFTER SHUTDOWN")
            pm(A,humans)
            input()

        #3 t번 사람이 근처 베이스캠프에 착륙
        if now_time <= M:
            new_hi = now_time
            sr, sc = store[new_hi]
            br, bc = bfs_store(sr, sc, A)
            # if A[br][bc] == -1:
            #     print("출발 basecamp가 겹치긴 하는데... 조건 상 문제되진 않는 것 같네")
            A[br][bc] = -1
            humans.append((new_hi, br, bc))
        if DEBUG:
            print("AFTER BASECAMP ")
            pm(A,humans)
            input()

        if len(humans)==0:
            break
    return now_time

def pm(A, H):
    print("LOOK CLOSER !")
    for r in range(len(A)):
        for c in range(len(A)):
            e = A[r][c]

            tmp = []
            for hi, hr, hc in H:
                if (hr, hc) == (r, c):
                    tmp.append(hi)

            if e==0:
                if tmp:
                    print(tmp, end='\t')
                else:
                    print('.', end='\t')
            elif e==1:
                print("BC",end='')
                if tmp:
                    print(tmp, end='')
                print('\t',end='')
            elif e==2:
                print("G", end='')
                if tmp:
                    print(tmp, end='')
                print('\t',end='')
            elif e==-1:
                print("X", end='')
                if tmp:
                    print(tmp, end='')
                print('\t',end='')
        print()
    print()



def p(A):
    for l in A:
        for e in l:
            print(e, end=' ')
        print()
    print()

def get_nxt_loc(hr, hc, gr, gc, A):
    # (hr,hc)의 사람이, (gr,gc)에 가기 위한 다음 최단 위치 반환
    diff = [(-1,0),(0,-1),(0,1),(1,0)]  # priority
    N = len(A)
    min_dist = 1e6
    final_nxt_hr, final_nxt_hc = None, None
    for dr,dc in diff:
        nxt_hr, nxt_hc = hr+dr, hc+dc
        if 0<=nxt_hr<N and 0<=nxt_hc<N and A[nxt_hr][nxt_hc]!=-1:
            if (nxt_hr, nxt_hc) == (gr,gc):
                return gr, gc
            dist = get_dist(nxt_hr,nxt_hc,gr,gc,A)
            if dist < min_dist:
                min_dist = dist
                final_nxt_hr = nxt_hr
                final_nxt_hc = nxt_hc
    if final_nxt_hr==None:
        raise Exception("ERROR")
    return final_nxt_hr, final_nxt_hc

def get_dist(hr,hc,gr,gc,A):

    diff = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # priority
    N = len(A)
    A_debug = [line.copy() for line in A]
    A_debug[hr][hc] = 'S'
    visit = [[0]*N for _ in range(N)]
    visit[hr][hc] = 1

    dq = [(hr,hc)]
    dist = 0
    while dq:
        dist += 1
        nxt_dq = []
        for cr,cc in dq:
            for dr,dc in diff:
                nr, nc = cr+dr, cc+dc
                if 0 <= nr < N and 0 <= nc < N and A[nr][nc] != -1 and visit[nr][nc]==0:
                    if (nr,nc) == (gr,gc):
                        return dist
                    A_debug[nr][nc] = 'V'
                    visit[nr][nc] = 1
                    nxt_dq.append((nr,nc))
        dq = nxt_dq

    # 편의점에 절대 도달 못하지만, 다른 경우의 수에서 편의점에 바로 도달할거기에, 거리를 max로 준다.
    return 1e6

def bfs_store(sr, sc, A):
    # 근처 basecamp 찾아줌
    diff = [(1,0),(-1,0),(0,1),(0,-1)]
    N = len(A)

    basecamp = []
    A_debug = [line.copy() for line in A]
    visit = [[0]*N for _ in range(N)]
    visit[sr][sc] = 1

    dq = [(sr,sc)]
    end_flag = False
    while dq:
        nxt_dq = []
        for sr,sc in dq:
            for dr,dc in diff:
                nr,nc = sr+dr, sc+dc
                if 0<=nr<N and 0<=nc<N and A[nr][nc]>=0 and visit[nr][nc]==0:
                    if A[nr][nc] == 1:
                        visit[nr][nc] = 1
                        basecamp.append((nr,nc))
                        end_flag = True
                        A_debug[nr][nc] = "B"
                    else:
                        nxt_dq.append((nr,nc))
                        visit[nr][nc] = 1
                        A_debug[nr][nc] = "V"
        dq = nxt_dq
        if end_flag:
            break

    basecamp.sort(key=lambda x:(x[0],x[1]))
    br, bc = basecamp[0]
    return br,bc

print(solution(False))