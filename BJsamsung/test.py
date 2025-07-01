from collections import deque

def magic(A, l):  # O(64)
    global N
    if l > 0:
        for r_st in range(0, 2 ** N, 2 ** l):
            for c_st in range(0, 2 ** N, 2 ** l):

                chunk = []
                for r_cur in range(r_st, r_st + 2 ** l):
                    chunk.append(A[r_cur][c_st:c_st + 2 ** l])
                chunk.reverse()
                chunk = list(zip(*chunk))

                for r_cur in range(r_st, r_st + 2 ** l):
                    A[r_cur][c_st:c_st + 2 ** l] = chunk[r_cur - r_st]


def ice_loss(A):
    # magic에서 계산량 적어서, 전수조사 해본다.
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    B=[[-1]*len(A) for _ in range(len(A))]

    for r in range(len(A)):
        for c in range(len(A)):
            count=0
            for di in range(4):
                nr,nc = r+dr[di], c+dc[di]
                if not (0<=nr<len(A) and 0<=nc<len(A)):
                    count+=1
                elif A[nr][nc]==0:
                    count+=1
            if count>=2:
                B[r][c] = max(0,A[r][c]-1)
            else:
                B[r][c] = A[r][c]
    return B

def find_largest_chunk(A):
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    lcs = 0
    chk = [[0]*len(A) for _ in range(len(A))]

    for r in range(len(A)):
        for c in range(len(A)):
            if chk[r][c]==1 or A[r][c]==0:
                continue
            chk[r][c] = 1
            dq = deque()
            dq.append((r,c))
            count = 0
            while dq:
                r,c = dq.popleft()
                count += 1
                for di in range(4):
                    nr, nc = r+dr[di], c+dc[di]
                    if 0 <= nr < len(A) and 0 <= nc < len(A):
                        if chk[nr][nc]==0 and A[nr][nc]>0:
                            chk[nr][nc]=1
                            dq.append((nr,nc))

            lcs = max(lcs, count)
    return lcs

def p(arr):
    for l in arr:
        for e in l:
            print(e, end='\t')
        print()
    print()


N = 3
A = [[i for i in range(n,n+2**N)] for n in range(0,2**(N*2),2**N)]

B = [list(map(int, input().split())) for _ in range(7)]

print(find_largest_chunk(B))