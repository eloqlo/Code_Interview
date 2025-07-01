def p(A):
    print()
    for l in A:
        for e in l:
            print(e, end=' ')
        print()

def solution():
    R,C,K = map(int,input().split())
    G = []
    for _ in range(K):
        c,d = map(int,input().split())
        G.append((c-1,d))
    exit_diff = [(-1,0),(0,1),(1,0),(0,-1)]
    A = [[0]*C for _ in range(R+3)]
    golems = {}
    SCORE = 0

    for cur_golem_idx in range(1, K + 1):
        cur_c, cur_d = G[cur_golem_idx - 1]
        for cur_r in range(1,R+2):
            if cur_r==R+1:
                break

            if A[cur_r+1][cur_c-1] + A[cur_r+1][cur_c+1] + A[cur_r+2][cur_c]==0:
                continue
            if cur_c>=2:
                if A[cur_r-1][cur_c-1]+A[cur_r][cur_c-2]+A[cur_r+1][cur_c-1]+ \
                        A[cur_r+1][cur_c-2]+A[cur_r+2][cur_c-1]==0:
                    cur_c -= 1
                    cur_d = (cur_d-1+4) % 4
                    continue
            if cur_c<=C-3:
                if A[cur_r-1][cur_c+1]+A[cur_r][cur_c+2]+A[cur_r+1][cur_c+1]+ \
                        A[cur_r+1][cur_c+2]+A[cur_r+2][cur_c+1]==0:
                    cur_c += 1
                    cur_d = (cur_d+1) % 4
                    continue
            break

        if cur_r <= 3:
            A = [[0] * C for _ in range(R + 3)]
            golems={}
            continue

        if A[cur_r][cur_c]!=0:
            raise Exception
        A[cur_r][cur_c] = cur_golem_idx
        for dr,dc in exit_diff:
            if A[cur_r + dr][cur_c + dc] != 0:
                raise Exception
            A[cur_r + dr][cur_c + dc] = cur_golem_idx
        golems[cur_golem_idx] = [cur_r,cur_c,cur_d]

        # BFS
        """
        타고 갈 수 있는 애들 중, 가장 낮은 위치 찾기
        """
        foo = [cur_golem_idx]
        visit = [cur_golem_idx]
        max_row = 0
        while foo:
            tmp_golem_idx = foo.pop()
            tmpr, tmpc, tmpd = golems[tmp_golem_idx]
            max_row = max(max_row, tmpr)
            if max_row == R+1:
                break
            exitr, exitc = tmpr + exit_diff[tmpd][0], tmpc + exit_diff[tmpd][1]
            for dr,dc in exit_diff:
                sr,sc = exitr+dr, exitc+dc
                if 0<=sr<R+2 and 0<=sc<C:
                    if (A[sr][sc] not in visit) and A[sr][sc] != 0:
                        visit.append(A[sr][sc])
                        foo.append(A[sr][sc])
        SCORE += max_row-1

    return SCORE

print(solution())