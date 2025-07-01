from collections import deque

def find_chunk(A):   # -> 기준블록 위치
    chk=[[0]*len(A) for _ in range(len(A))]
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    max_size = 1
    max_r, max_c = None, None
    max_rainbow_size = 0

    for r in range(len(A)):
        for c in range(len(A)):
            if chk[r][c] == 1:
                continue
            color = A[r][c]
            chk[r][c] = 1   # 전체 돌면서 중복방지
            if color == None:
                continue

            if color >= 1:
                size = 0
                rainbow_size = 0
                norm_r, norm_c = r, c
                dq = deque()
                dq.append((r,c))
                visited = set()   # 한 chunk에서 중복방지
                visited.add((r,c))

                while dq:
                    search_r,search_c = dq.popleft()
                    if norm_r>search_r and A[search_r][search_c]==color:
                        norm_r, norm_c = search_r, search_c
                    if norm_r==search_r and norm_c>search_c and A[search_r][search_c]==color:
                        norm_r,norm_c = search_r,search_c
                    size += 1
                    for di in range(4):
                        nr, nc = search_r + dr[di], search_c + dc[di]
                        if 0 <= nr < len(A) and 0 <= nc < len(A):
                            #1 조회하지 않은 color 블록
                            if A[nr][nc] == color and ((nr,nc) not in visited):
                                chk[nr][nc] = 1
                                visited.add((nr, nc))
                                dq.append((nr,nc))
                            #2 그냥 무지개 블록
                            elif A[nr][nc] == 0 and ((nr,nc) not in visited):
                                rainbow_size += 1
                                chk[nr][nc] = 1
                                visited.add((nr, nc))
                                dq.append((nr, nc))

                if size != len(visited):
                    print(size, len(visited))
                    raise Exception("ERROR")
                if size > max_size:
                    max_size = size
                    max_rainbow_size = rainbow_size
                    max_r, max_c = norm_r, norm_c
                elif size==max_size and size>1:
                    if max_rainbow_size < rainbow_size:
                        max_size = size
                        max_rainbow_size = rainbow_size
                        max_r, max_c = norm_r, norm_c
                    elif max_rainbow_size == rainbow_size:
                        if max_r < norm_r:
                            max_size = size
                            max_rainbow_size = rainbow_size
                            max_r, max_c = norm_r, norm_c
                        elif max_r==norm_r:
                            if max_c<norm_c:
                                max_size = size
                                max_rainbow_size = rainbow_size
                                max_r, max_c = norm_r, norm_c

    if max_size>1:
        if max_r==None:
            raise Exception("E2 Chunk는 찾는데, 기준좌표가 업데이트 안됨")
        return max_r, max_c
    else:
        if max_r!=None:
            raise Exception("E3")
        return None, None


def pop_and_score(r,c,A):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    dq = deque()
    dq.append((r, c))
    color = A[r][c]
    score = 0
    A[r][c] = None
    while dq:
        r, c = dq.popleft()
        score+=1
        for di in range(4):
            nr, nc = r + dr[di], c + dc[di]
            if 0<=nr<len(A) and 0<=nc<len(A):
                if A[nr][nc] == color or A[nr][nc] == 0:
                    dq.append((nr,nc))
                    A[nr][nc] = None
    return score**2

def gravity_and_rotation(A):
    def cw(A):
        A.reverse()
        A = list(zip(*A))
        return [list(line) for line in A]
    def ccw(B):
        B = list(zip(*B))
        B.reverse()
        return [list(line) for line in B]
    def gravity_left(A):
        B=[]
        for line in A:
            new_line=[]
            tmp=[]
            none_count=0
            for e in line:
                if e==None:
                    none_count+=1
                    continue
                elif e==-1:
                    new_line += tmp + [None]*none_count + [-1]
                    none_count=0
                    tmp=[]
                else:
                    tmp.append(e)
            new_line += tmp + [None]*none_count
            B.append(new_line)
        return B

    return ccw(gravity_left(ccw(gravity_left(cw(A)))))

def p(A):
    for l in A:
        for e in l:
            print(e, end='\t')
        print()
    print()

N,M = map(int,input().split())
A = []
score=0
for _ in range(N):
    A.append(list(map(int,input().split())))
for _ in range(20000000):

    r,c = find_chunk(A)
    if r==None:
        break
    score += pop_and_score(r,c,A)
    A = gravity_and_rotation(A)

print(score)