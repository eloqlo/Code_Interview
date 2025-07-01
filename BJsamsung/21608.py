N=int(input())
students={}
for _ in range(N**2):
    num, n1,n2,n3,n4 = map(int,input().split())
    students[num] = (n1,n2,n3,n4)
A=[[0]*N for _ in range(N)]

dr=[-1,0,0,1]
dc=[0,-1,1,0]
for s in students:
    like = students[s]
    max_like=0
    max_zero=0
    fr,fc = None,None
    tmp_flag = True
    for r in range(N):
        for c in range(N):
            like_count = 0
            zer_count = 0
            if A[r][c]==0:
                if tmp_flag:
                    tmp_flag = False
                    tr,tc = r,c
                for di in range(4):
                    nr,nc = r+dr[di], c+dc[di]
                    if 0<=nr<N and 0<=nc<N:
                        if A[nr][nc] in like:
                            like_count += 1
                        if A[nr][nc] == 0:
                            zer_count+=1

                if max_like<like_count:
                    max_like= like_count
                    max_zero = zer_count
                    fr,fc = r,c
                elif max_like==like_count and max_zero<zer_count:
                    max_zero=zer_count
                    fr,fc = r,c
    if fr==None:
        A[tr][tc] = s
    else:
        A[fr][fc] = s

total_count=0
for r in range(N):
    for c in range(N):
        ele = A[r][c]
        count = 0
        for di in range(4):
            nr, nc = r + dr[di], c + dc[di]
            if 0 <= nr < N and 0 <= nc < N:
                if A[nr][nc] in students[ele]:
                    count+=1
        if count>0:
            total_count += 10**(count-1)

print(total_count)