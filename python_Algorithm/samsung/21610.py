def p(A):
    for l in A:
        for e in l:
            print(e, end=' ')
        print()
    print()
def solution():
    N,M = map(int, input().split())
    A=[]
    mv=[]
    for _ in range(N):
        A.append(list(map(int,input().split())))
    for _ in range(M):
        d,s=map(int,input().split())
        mv.append([d-1,s])
    dr=[0,-1,-1,-1,0,1,1,1]
    dc=[-1,-1,0,1,1,1,0,-1]
    diag_r=[-1,-1,1,1]
    diag_c=[-1,1,-1,1]

    cr, cc = N-2, 0
    cloud_loc = [(cr,cc),
                 ((cr+1)%N,cc),
                 ((cr+1)%N,(cc+1)%N),
                 (cr,(cc+1)%N)]
    for idx in range(M):
        d,s = mv[idx]
        new_cloud_loc=[]

        # rain
        for ci in range(len(cloud_loc)):
            cr, cc = cloud_loc[ci]
            nr, nc = cr+dr[d]*s, cc+dc[d]*s
            nr,nc = (nr + N*30)%N, (nc + N*30)%N
            A[nr][nc]+=1
            new_cloud_loc.append((nr,nc))

        # increase water
        for ci in range(len(new_cloud_loc)):
            cr, cc = new_cloud_loc[ci]
            water_bucket_count=0
            for di in range(4):
                nr,nc = cr+diag_r[di], cc+diag_c[di]
                if 0<=nr<N and 0<=nc<N:
                    if A[nr][nc]:
                        water_bucket_count+=1
            A[cr][cc]+=water_bucket_count

        # make cloud
        new_cloud_loc = set(new_cloud_loc)
        cloud_loc = []
        for r in range(N):
            for c in range(N):
                if A[r][c]>=2:
                    if (r,c) not in new_cloud_loc:
                        cloud_loc.append((r,c))
                        A[r][c]-=2
        # p(A)

    water_amount = sum([sum(line) for line in A])
    return water_amount

print(solution())