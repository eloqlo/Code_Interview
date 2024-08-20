from collections import defaultdict

def p(A):
    for l in A:
        for e in l:
            print(e, end=' ')
        print()
    print()

def solution():
    N,K = map(int,input().split())
    A = []
    vir = defaultdict(list)
    for r in range(N):
        line = []
        for c, ele in enumerate(map(int,input().split())):
            line.append(ele)
            if ele > 0:
                vir[ele].append((r,c))
        A.append(line)
    S, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    for _ in range(S):
        nxt_vir = defaultdict(list)
        for vir_num in vir.keys():
            vir_loc_arr = vir[vir_num]
            for r,c in vir_loc_arr:
                for di in range(4):
                    nr,nc = r+dr[di], c+dc[di]
                    if 0 <= nr < N and 0 <= nc < N:
                        if A[nr][nc] == 0:
                            A[nr][nc] = vir_num
                            nxt_vir[vir_num].append((nr,nc))
        vir = nxt_vir
    return A[X][Y]

print(solution())