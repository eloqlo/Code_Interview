def p(A):
    for l in A:
        for e in l:
            if e!=[]:
                for ee in e:
                    print(ee, end=' ')
                print('\t',end='')
            else:
                print('.',end='\t')
        print()
    print()

def ps(A,sr,sc):
    for r in range(4):
        for c in range(4):
            if (r,c)==(sr,sc):
                print("S",end='')
            if A[r][c] != []:
                for e in A[r][c]:
                    print(e, end=' ')
                print('\t', end='')
            else:
                print('.', end='\t')
        print()
    print()

def solution():
    M,S = map(int,input().split())
    A=[]
    for _ in range(4):
        line=[]
        for _ in range(4):
            line.append([])
        A.append(line)
    for _ in range(M):
        fx,fy,d = map(int,input().split())
        A[fx-1][fy-1].append(d-1)
    sr,sc = map(int,input().split())
    sr-=1; sc-=1
    dr=[0,-1,-1,-1,0,1,1,1]
    dc=[-1,-1,0,1,1,1,0,-1]
    dsr=[-1,0,1,0]
    dsc=[0,-1,0,1]

    smell_cur = set()
    smell1 = set()
    smell2 = set()
    def fish_move_condition(fr,fc):
        if not (0<=fr<4 and 0<=fc<4):
            return False
        elif (fr,fc)==(sr,sc):
            return False
        elif (fr,fc) in smell1:
            return False
        elif (fr,fc) in smell2:
            return False
        return True

    for step in range(S):
        A_new = []
        for _ in range(4):
            line = []
            for _ in range(4):
                line.append([])
            A_new.append(line)

        #1 MOVE
        for r in range(4):
            for c in range(4):
                for d_fish in A[r][c]:
                    break_flag=False
                    for coef in range(8):
                        tmp_d_fish = (d_fish-coef + 8)%8
                        nr, nc = r+dr[tmp_d_fish], c+dc[tmp_d_fish]
                        if fish_move_condition(nr, nc):
                            A_new[nr][nc].append(tmp_d_fish)
                            break_flag = True
                            break
                    if break_flag!=True:
                        A_new[r][c].append(d_fish)

        #2 SHARK MOVE
        max_fish = 0
        max_loc = None
        for s_d1 in range(4):
            cur_fish_count = 0
            tmp_sr1, tmp_sc1 = sr+dsr[s_d1], sc+dsc[s_d1]
            if not (0 <= tmp_sr1 < 4 and 0 <= tmp_sc1 < 4):
                continue
            cur_fish_count += len(A_new[tmp_sr1][tmp_sc1])
            step1_fish_tmp = A_new[tmp_sr1][tmp_sc1]
            A_new[tmp_sr1][tmp_sc1] = []

            for s_d2 in range(4):
                tmp_sr2, tmp_sc2 = tmp_sr1 + dsr[s_d2], tmp_sc1 + dsc[s_d2]
                if not (0 <= tmp_sr2 < 4 and 0 <= tmp_sc2 < 4):
                    continue
                cur_fish_count += len(A_new[tmp_sr2][tmp_sc2])
                step2_fish_tmp = A_new[tmp_sr2][tmp_sc2]
                A_new[tmp_sr2][tmp_sc2] = []

                for s_d3 in range(4):
                    tmp_sr3, tmp_sc3 = tmp_sr2 + dsr[s_d3], tmp_sc2 + dsc[s_d3]
                    if not (0 <= tmp_sr3 < 4 and 0 <= tmp_sc3 < 4):
                        continue
                    cur_fish_count += len(A_new[tmp_sr3][tmp_sc3])
                    step3_fish_tmp = A_new[tmp_sr3][tmp_sc3]
                    A_new[tmp_sr3][tmp_sc3] = []

                    if max_loc == None:
                        max_loc = [(tmp_sr1, tmp_sc1), (tmp_sr2, tmp_sc2), (tmp_sr3, tmp_sc3)]
                    if max_fish < cur_fish_count:
                        max_loc = [(tmp_sr1,tmp_sc1),(tmp_sr2,tmp_sc2),(tmp_sr3,tmp_sc3)]
                        max_fish = cur_fish_count

                    A_new[tmp_sr3][tmp_sc3] = step3_fish_tmp
                    cur_fish_count -= len(A_new[tmp_sr3][tmp_sc3])
                A_new[tmp_sr2][tmp_sc2] = step2_fish_tmp
                cur_fish_count -= len(A_new[tmp_sr2][tmp_sc2])
            A_new[tmp_sr1][tmp_sc1] = step1_fish_tmp
            cur_fish_count -= len(A_new[tmp_sr1][tmp_sc1])
        if cur_fish_count!=0:
            raise Exception

        for max_sr, max_sc in max_loc:
            if len(A_new[max_sr][max_sc]) > 0:
                smell_cur.add((max_sr, max_sc))
                A_new[max_sr][max_sc] = []
        sr, sc = max_loc[-1][0], max_loc[-1][1]

        #3 FISH TRAIL Vanish
        smell2 = smell1
        smell1 = smell_cur
        smell_cur = set()

        #4 FISH Duplicated
        for r in range(4):
            for c in range(4):
                A[r][c] += A_new[r][c]
        #for end
        #glue
    #glue
    # p(A)
    answer = 0
    for r in range(4):
        for c in range(4):
            answer += len(A[r][c])

    return answer

print(solution())