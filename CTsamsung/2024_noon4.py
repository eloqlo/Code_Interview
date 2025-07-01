def p(A):
    print()
    for l in A:
        for e in l:
            print(e, end=' ')
        print()
    return

def solution():
    R,C,K = map(int, input().split())
    golems_info=[]
    for _ in range(K):
        c,d = map(int, input().split())
        golems_info.append((c-1,d))
    diff = [(-1,0),(0,1),(1,0),(0,-1)]

    A = [[0]*C for _ in range(R+3)]
    cur_golems_info = {}
    SCORE = 0


    for golem_idx, (cur_c, cur_d) in enumerate(golems_info):
        # 최저로 내려가기
        for cur_r in range(1,R+2):
            if cur_r == R+1:
                break

            if A[cur_r+2][cur_c]+A[cur_r+1][cur_c-1]+A[cur_r+1][cur_c+1]==0:
                continue
            if cur_c >= 2 and A[cur_r-1][cur_c-1] + A[cur_r][cur_c-2] + A[cur_r+1][cur_c-1] + A[cur_r+1][cur_c-2] + A[cur_r+2][cur_c-1] == 0:
                cur_c-=1
                cur_d = (cur_d+3)%4
                continue
            if cur_c <= C-3 and A[cur_r-1][cur_c+1] + A[cur_r][cur_c+2] + A[cur_r+1][cur_c+1] + A[cur_r+1][cur_c+2] + A[cur_r+2][cur_c+1] == 0:
                cur_c+=1
                cur_d = (cur_d+1)%4
                continue
            break

        # 튀어나왔으면 초기화
        if cur_r <= 3:
            A = [[0] * C for _ in range(R + 3)]
            cur_golems_info = {}
            continue

        # 맵에 기록
        golem_idx += 1
        cur_golems_info[golem_idx] = (cur_r, cur_c, cur_d)
        if A[cur_r][cur_c]!=0:
            raise Exception()
        A[cur_r][cur_c] = golem_idx
        for dr,dc in diff:
            if A[cur_r + dr][cur_c + dc] != 0:
                raise Exception()
            A[cur_r + dr][cur_c + dc] = golem_idx

        # BFS로 최저점 찾기
        dq = [golem_idx]
        visit = set([golem_idx])
        max_row = 0
        while dq:
            gi = dq.pop()
            tmpr, tmpc, tmpd = cur_golems_info[gi]
            max_row = max(max_row, tmpr-1)
            if tmpr == R+1:
                break
            er,ec = tmpr + diff[tmpd][0], tmpc + diff[tmpd][1]
            for dr, dc in diff:
                nr, nc = er + dr, ec + dc
                if 0 <= nr < R+2 and 0 <= nc < C and A[nr][nc]!=0 and A[nr][nc] not in visit:
                    visit.add(A[nr][nc])
                    dq.append(A[nr][nc])

        # 점수 업데이트
        SCORE += max_row

    return SCORE

print(solution())

# T = int(input())
# ans=[]
# for test in range(T):
#     ans.append(solution())
# for test in range(1,T+1):
#     print(f"#{test} {ans[test-1]}")