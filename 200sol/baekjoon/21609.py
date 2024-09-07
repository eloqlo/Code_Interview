def p(A):
    print()
    for l in A:
        for e in l:
            print(e, end='\t')
        print()
    print()
def find_group(A):

    size = {}
    visit = [[0]*len(A) for _ in range(len(A))]
    diff = [(1,0),(-1,0),(0,1),(0,-1)]
    N = len(A)
    foo = []

    for r in range(len(A)):
        for c in range(len(A)):
            if A[r][c]==None:
                continue
            if not (A[r][c]>0 and visit[r][c]==0):
                continue
            visit[r][c] = 1
            total_size = 1
            rainbow_size = 0
            search = [(r,c)]

            while search:
                cr,cc = search.pop()
                for dr,dc in diff:
                    nr,nc = cr+dr, cc+dc
                    if 0<=nr<N and 0<=nc<N and A[nr][nc]!=-1 and visit[nr][nc]==0:
                        if A[nr][nc]==0 or A[nr][nc]==A[r][c]:
                            visit[nr][nc] = 1
                            search.append((nr,nc))
                            total_size += 1
                            if A[nr][nc]==0:
                                rainbow_size += 1
            if total_size>=2:
                foo.append((total_size,rainbow_size,r,c))

    if foo:
        foo.sort(key=lambda x:(-x[0],-x[1],-x[2],-x[3]))
        return foo[0][2], foo[0][3]
    else:
        return None, None

def delete_group(A,r,c):

    diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    N = len(A)
    size = 0
    color = A[r][c]

    dq = [(r,c)]
    visit = set()
    while dq:
        r,c = dq.pop()
        visit.add((r,c))
        A[r][c] = None
        size += 1
        for dr,dc in diff:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and (A[nr][nc] == color or A[nr][nc]==0) and (nr,nc) not in visit:
                dq.append((nr, nc))
                visit.add((nr,nc))
    return A, size


def gravity(A):
    N = len(A)

    # CCW
    A = list(zip(*A))[::-1]

    new_A = []
    for line in A:
        new_line = []
        tmp = []
        size = 0
        for ele in line:
            size += 1
            if ele==None:
                continue
            tmp.append(ele)
            if ele==-1:
                new_line += [None]*(size-len(tmp)) + tmp
                size=0
                tmp = []
        new_line += [None]*(size-len(tmp)) + tmp
        new_A.append(new_line)
    # CW
    A = list(map(list,zip(*new_A[::-1])))

    return A

def solution():
    N,M = map(int, input().split())
    A = []
    for _ in range(N):
        line = list(map(int, input().split()))
        A.append(line)

    """
    1. 크기가 제일 큰 블록 그룹 찾기
    2. 그 그룹 블록 제거/ 개수**2 만큼 점수 획득
    3. 중력!
    4. -90도 회전
    5. 중력!
    """
    SCORE = 0
    while True:
        cr,cc = find_group(A)
        if cr==None:
            break
        A, score = delete_group(A,cr,cc)
        SCORE += score**2

        A = gravity(A)
        A = list(map(list,zip(*A)))[::-1]
        A = gravity(A)


    return SCORE

print(solution())

