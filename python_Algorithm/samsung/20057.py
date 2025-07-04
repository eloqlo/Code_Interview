def solution():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    mr=[0,1,0,-1]
    mc=[-1,0,1,0]
    dr=[-1,-1,-1,1,1,1,-2,0,2,0]
    dc=[1,0,-1,-1,0,1,0,-2,0,-1]
    da=[1,7,10,10,7,1,2,5,2,None]
    dr2=[-1,-1,-1,0,1,1,1,0,-2,0,2,0]
    dc2=[1,0,-1,-1,-1,0,1,1,0,-2,0,2]

    answer = 0
    r, c = N//2, N//2
    mv = 1
    for dx in range(250000):
        di = dx%4
        for _ in range(mv):
            r,c = r+mr[di], c+mc[di]
            if not (0<=r<N and 0<=c<N):
                return answer

            y = arr[r][c]
            arr[r][c]=0
            arr2 = [[0]*5 for _ in range(5)]
            amount_count=0
            for di2 in range(10):
                r2,c2 = 2+dr[di2], 2+dc[di2]
                if not di2==9:
                    amount = int(y*(da[di2]*0.01))
                    arr2[r2][c2] = amount
                    amount_count += amount
                else:
                    arr2[r2][c2] = y - amount_count

            # arr2회전
            if di==0:
                pass
            elif di==1:
                arr2 = list(zip(*arr2))
                arr2.reverse()
            elif di==2:
                arr3=[]
                for line in arr2:
                    line.reverse()
                    arr3.append(line)
                arr2=arr3
            elif di==3:
                arr2.reverse()
                arr2 = list(zip(*arr2))

            # arr2 arr에 대입
            for di2 in range(12):
                r2,c2 = 2+dr2[di2], 2+dc2[di2]
                nr,nc = r+dr2[di2], c+dc2[di2]
                y = arr2[r2][c2]
                if 0<=nr<N and 0<=nc<N:
                    arr[nr][nc] += y
                else:
                    answer += y

            # p(r,c,arr)

        if not dx%2==0:
            mv+=1
    return answer

def p(r,c,arr):
    print(f"_____r:{r}, c:{c}_____")
    for l in arr:
        for e in l:
            print(e, end='\t')
        print()

print(solution())