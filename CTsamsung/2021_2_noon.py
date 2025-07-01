def solution():

    # INPUTS
    N = 4
    M, T = map(int, input().split())
    pr, pc = map(int, input().split())
    pr -= 1; pc -= 1
    A = [[[] for _ in range(N)] for _ in range(N)]
    Ad = [[[] for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        mr,mc,md = map(int,input().split())
        mr-=1; mc-=1; md-=1
        # monsters[mi] = [mr,mc,md]
        A[mr][mc].append(md)

    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,-1,-1,-1,0,1,1,1]
    dpr = [-1, 0, 1, 0]
    dpc = [0, -1, 0, 1]
    dead_loc1 = set()
    dead_loc2 = set()

    # print("INIT")
    # p(A,pr,pc)
    # input()

    for _ in range(T):

        B = [[[] for _ in range(N)] for _ in range(N)]

        # MOVE
        for r in range(4):
            for c in range(4):
                for md in A[r][c]:
                    monster_updated = False
                    for foo in range(8):
                        new_md = (md + foo) % 8
                        nr, nc = r+dr[new_md], c+dc[new_md]
                        if (0 <= nr < N and 0 <= nc < N and
                                (nr, nc) not in dead_loc1 and
                                (nr, nc) not in dead_loc2 and
                                (nr, nc) != (pr, pc)):
                            B[nr][nc].append(new_md)
                            monster_updated = True
                            break
                    if not monster_updated:
                        B[r][c].append(md)

        # print("AF MOVE")
        # p(B,pr,pc)
        # input()

        # pac-man MOVE
        dead_loc0 = set()
        best_order = get_best_move(B, pr, pc)
        for pd in best_order:
            pr, pc = pr+dpr[pd], pc+dpc[pd]
            if B[pr][pc]:
                B[pr][pc] = []
                dead_loc0.add((pr,pc))

        # print("PAC MOVE")
        # p(B,pr,pc)
        # input()

        # 시체 소멸
        dead_loc2 = dead_loc1
        dead_loc1 = dead_loc0

        # 복제 반영
        for r in range(4):
            for c in range(4):
                A[r][c] += B[r][c]


        # print("복제 결과")
        # p(A,pr,pc)
        # print("________________________")
        # input()


    answer = 0
    for l in A:
        for e in l:
            answer += len(e)
    return answer


def get_best_move(A,pr,pc):
    dr = [-1,0,1,0]
    dc = [0,-1,0,1]

    best_order = []
    zero_order = []
    max_count = 0

    for d1 in range(4):
        nr1, nc1 = pr+dr[d1], pc+dc[d1]
        if 0 <= nr1 < 4 and 0 <= nc1 < 4:

            for d2 in range(4):
                nr2, nc2 = nr1 + dr[d2], nc1 + dc[d2]
                if 0 <= nr2 < 4 and 0 <= nc2 < 4:

                    for d3 in range(4):
                        nr3, nc3 = nr2 + dr[d3], nc2 + dc[d3]
                        if 0 <= nr3 < 4 and 0 <= nc3 < 4:

                            count = len(A[nr1][nc1]) + len(A[nr2][nc2])
                            if (nr3,nc3) not in [(nr1,nc1),(nr2,nc2)]:
                                count += len(A[nr3][nc3])

                            if len(zero_order)==0 and max_count==0:
                                zero_order = [d1,d2,d3]

                            if count > max_count:
                                max_count = count
                                best_order = [d1,d2,d3]

    if max_count==0:
        return zero_order
    return best_order

def p(A,pr,pc):
    for r,l in enumerate(A):
        for c,e in enumerate(l):

            if (r,c)==(pr,pc):
                print('S',end='')

            if e:
                print(','.join(list(map(str,e))), end='\t')
            else:
                print('.', end='\t')
        print()


print(solution())