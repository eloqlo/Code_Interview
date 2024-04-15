N = int(input())
arr = [[0] * N for _ in range(N)]

dr = [0,1,0,-1]
dc = [-1,0,1,0]
r = N//2
c = N//2

count = 0
val=1
di=0
while val<N*N:
    di = count%4
    for _ in range(count//2 + 1):
        r = r + dr[di]
        c = c + dc[di]
        arr[r][c] = val
        val+=1
        if val==N*N:
            break
    count += 1

for line in arr:
    print(line)