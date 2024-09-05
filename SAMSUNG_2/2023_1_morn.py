def p(A):
    print()
    for l in A:
        for e in l:
            print(e, end='\t')
        print()
    print()


def pt(A, li, wr,wc,sr,sc):
    print()
    for r in range(len(A)):
        for c in range(len(A[0])):
            if (r,c)==(wr,wc):
                print(f"<{A[r][c]}>", end='\t')
            elif (r,c)==(sr,sc):
                print(f"+{A[r][c]}+", end='\t')
            elif (r,c) in li:
                print(f"({A[r][c]})", end='\t')
            else:
                print(A[r][c], end='\t')
        print()
    print()


#TODO 이거 더 간단히 코딩 못하려나? 헷갈린다.
"""
공격자, 피격자 선정 조건이 가독성 떨어져서 충분히 조건체크가 안됐다.
"""
def find_weak_strong(A, B):
    low_atk = 1e6
    low_atk_recent_turn = None
    low_atk_rpc = None
    low_atk_col = None

    high_atk = -1
    high_atk_old_turn = None
    high_atk_rpc = None
    high_atk_col = None

    wr, wc = None, None
    sr, sc = None, None

    for r in range(len(A)):
        for c in range(len(A[0])):
            if A[r][c] > 0:
                if A[r][c] > high_atk:
                    high_atk = A[r][c]
                    high_atk_old_turn = B[r][c]
                    high_atk_rpc = r + c
                    high_atk_col = c
                    sr, sc = r, c
                elif A[r][c] == high_atk:
                    if B[r][c] < high_atk_old_turn:
                        high_atk = A[r][c]
                        high_atk_old_turn = B[r][c]
                        high_atk_rpc = r + c
                        high_atk_col = c
                        sr, sc = r, c
                    elif B[r][c] == high_atk_old_turn:
                        if r + c < high_atk_rpc:
                            high_atk = A[r][c]
                            high_atk_old_turn = B[r][c]
                            high_atk_rpc = r + c
                            high_atk_col = c
                            sr, sc = r, c
                        elif r + c == high_atk_rpc:
                            if c < high_atk_col:
                                high_atk = A[r][c]
                                high_atk_old_turn = B[r][c]
                                high_atk_rpc = r + c
                                high_atk_col = c
                                sr, sc = r, c

                if A[r][c] < low_atk:
                    low_atk = A[r][c]
                    low_atk_recent_turn = B[r][c]
                    low_atk_rpc = r + c
                    low_atk_col = c
                    wr, wc = r, c
                elif A[r][c] == low_atk:
                    if B[r][c] > low_atk_recent_turn:
                        low_atk = A[r][c]
                        low_atk_recent_turn = B[r][c]
                        low_atk_rpc = r + c
                        low_atk_col = c
                        wr, wc = r, c
                    elif B[r][c] == low_atk_recent_turn:
                        if low_atk_rpc < r + c:
                            low_atk = A[r][c]
                            low_atk_recent_turn = B[r][c]
                            low_atk_rpc = r + c
                            low_atk_col = c
                            wr, wc = r, c
                        elif low_atk_rpc == r + c:
                            if low_atk_col < c:
                                low_atk = A[r][c]
                                low_atk_recent_turn = B[r][c]
                                low_atk_rpc = r + c
                                low_atk_col = c
                                wr, wc = r, c

    return wr, wc, sr, sc

def find_weak_strong2(A,B):
    """
    여러 조건 고려하는건, 이렇게 sort해주면 덜 헷갈리는구나!
    """
    min_val, max_val = 1e6, -1
    for r in range(len(A)):
        for c in range(len(A[0])):
            if A[r][c] > 0 and A[r][c] > max_val:
                max_val = A[r][c]
            if A[r][c] > 0 and A[r][c] < min_val:
                min_val = A[r][c]

    min_arr = []
    max_arr = []
    for r in range(len(A)):
        for c in range(len(A[0])):
            if A[r][c] == min_val:
                min_arr.append((B[r][c], r+c, c, (r,c)))
            if A[r][c] == max_val:
                max_arr.append((B[r][c], r+c, c, (r,c)))

    min_arr.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    max_arr.sort(key=lambda x:(x[0],x[1],x[2]))
    _,_,_,(wr,wc) = min_arr[0]
    _,_,_,(sr,sc) = max_arr[0]

    return wr,wc,sr,sc


def find_route(A, wr, wc, sr, sc):
    N, M = len(A), len(A[0])
    C, timer = bfs(A, wr, wc, sr, sc)
    if C == None:
        return None

    track, _ = dfs(C, wr, wc, sr, sc, [(wr, wc)])
    return track

def dfs(C, r, c, sr, sc, track):
    diff = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상
    N, M = len(C), len(C[0])

    cur_time = C[r][c]
    for dr, dc in diff:
        nr, nc = r + dr, c + dc
        nr, nc = (nr + N) % N, (nc + M) % M
        if C[nr][nc] == cur_time + 1:
            if (nr, nc) == (sr, sc):
                return track + [(nr, nc)], True
            answer, end_flag = dfs(C, nr, nc, sr, sc, track + [(nr, nc)])
            if end_flag:
                return answer, end_flag

    return None, None


def bfs(A, wr, wc, sr, sc):
    diff = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상
    N, M = len(A), len(A[0])

    C = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    visit[wr][wc] = 1
    timer = 1
    dq = [(wr, wc)]
    while dq:
        nxt_dq = []
        for cr, cc in dq:
            C[cr][cc] = timer
            if (cr, cc) == (sr, sc):
                return C, timer
            for dr, dc in diff:
                nr, nc = cr + dr, cc + dc
                nr, nc = (nr + N) % N, (nc + M) % M
                if A[nr][nc] != 0 and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    nxt_dq.append((nr, nc))
        dq = nxt_dq
        timer += 1

    return None, None


def solution():
    # INPUTS
    N, M, K = map(int, input().split())
    A = []
    for _ in range(N):
        line = list(map(int, input().split()))
        A.append(line)
    B = [[0] * M for _ in range(N)]  # 공격한 턴 저장

    for turn_k in range(1, K + 1):
        # 공격자 선정
        wr, wc, sr, sc = find_weak_strong2(A, B)

        if wr == None or sr == None:
            return 0
        elif (wr, wc) == (sr, sc):
            break

        B[wr][wc] = turn_k
        A[wr][wc] += N+M

        # 최단 경로 찾기 - BFS
        track = find_route(A, wr, wc, sr, sc)
        ATK = A[wr][wc]
        got_hit = set([(wr, wc)])
        got_hit.add((sr, sc))

        if track == None:
            # 포탄 공격
            # TODO SANITY CHECK
            track = [(sr,sc)]
            A[sr][sc] = max(0, A[sr][sc] - ATK)
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                nr, nc = sr + dr, sc + dc
                nr, nc = (nr + N) % N, (nc + M) % M
                if (nr, nc) == (wr, wc):
                    continue
                A[nr][nc] = max(0, A[nr][nc] - ATK // 2)
                got_hit.add((nr, nc))
                track.append((nr,nc))
        else:
            # 레이저 공격
            for nr, nc in track[1:-1]:
                A[nr][nc] = max(0, A[nr][nc] - ATK // 2)
                got_hit.add((nr, nc))
            A[sr][sc] = max(0, A[sr][sc] - ATK)

        # 포탑 정비 - 공격자, 피격자 빼고 +1
        for tmpr in range(N):
            for tmpc in range(M):
                if A[tmpr][tmpc] > 0 and (tmpr, tmpc) not in got_hit:
                    A[tmpr][tmpc] += 1

    max_val = 0
    for line in A:
        max_val = max(max_val, max(line))
    return max_val


print(solution())