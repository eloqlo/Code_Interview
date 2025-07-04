def p(A):
    print()
    for l in A:
        for e in l:
            print(e, end='\t')
        print()
    print()
def find_group(A):

    # size = {}
    # visit = [[0]*len(A) for _ in range(len(A))]
    diff = [(1,0),(-1,0),(0,1),(0,-1)]
    N = len(A)
    foo = []

    for r in range(len(A)):
        for c in range(len(A)):
            if A[r][c]==None or A[r][c]==0 or A[r][c]==-1:
                continue
            # visit[r][c]=1
            total_size = 1
            rainbow_size = 0
            search = [(r,c)]
            color = A[r][c]
            chunk = set()
            chunk.add((r,c))

            while search:
                cr,cc = search.pop()
                for dr,dc in diff:
                    nr,nc = cr+dr, cc+dc
                    if 0<=nr<N and 0<=nc<N and A[nr][nc] in (color, 0) and (nr,nc) not in chunk:
                        # if A[nr][nc]==color:
                        #     visit[nr][nc]=1
                        search.append((nr,nc))
                        chunk.add((nr,nc))
                        total_size += 1
                        if A[nr][nc]==0:
                            rainbow_size += 1
            fr,fc = sorted(list(chunk), key=lambda x:(x[0],x[1]))[0]
            if total_size >= 2:
                foo.append((total_size, rainbow_size, fr, fc))

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
            if ele == None:
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

    SCORE = 0
    while True:
        cr,cc = find_group(A)
        # p(A)
        if cr==None:
            break
        A, score = delete_group(A,cr,cc)
        # p(A)
        SCORE += score**2

        A = gravity(A)
        # p(A)
        A = list(map(list,zip(*A)))[::-1]
        # p(A)
        A = gravity(A)
        # p(A)

        # print("________________________________")
        # print(SCORE, score**2)
        # input()


    return SCORE

print(solution())