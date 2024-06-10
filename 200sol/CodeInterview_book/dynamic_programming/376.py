N=int(input())
tri_arr=[[[0]*N] for _ in range(N)]  # 0.1MB
tmp_arr=[]
for i in range(N):
    inp_arr = list(map(int,input().split()))
    tri_arr[i][:len(inp_arr)] = inp_arr
    tmp_arr.append([0]*len(inp_arr))
tmp_arr[0][0] = tri_arr[0][0]

for r in range(1,N):
    m = len(tri_arr[r])
    for c in range(m):
        if c==0:
            tmp_arr[r][c] = tmp_arr[r-1][0] + tri_arr[r][0]     # 윗층 바로 위(처음)
        elif c==m-1:
            tmp_arr[r][c] = tmp_arr[r-1][c-1] + tri_arr[r][c]   # 윗층 바로 위 앞(끝)
        else:
            tmp_arr[r][c] = max(tmp_arr[r-1][c], tmp_arr[r-1][c-1]) + tri_arr[r][c]

print(max(tmp_arr[-1]))