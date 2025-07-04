def solution():
    global cmds, del_count, arr

    for x,d,k in cmds:
        rotate(x,d,k)
        # pm()
        no_update = find_modify()
        if del_count == N*M:
            # pm()
            return 0
        if no_update:
            avg = get_avg()
            for r in range(N):
                for c in range(M):
                    if arr[r][c]==0:
                        continue
                    elif arr[r][c] > avg:
                        arr[r][c] -= 1
                    elif arr[r][c] < avg:
                        arr[r][c] += 1
        # pm()
    tot=0
    for l in arr:
        tot += sum(l)
    return tot

def get_avg():
    global arr, del_count
    avg = 0
    for l in arr:
        avg += sum(l)
    return avg/(N * M - del_count)

def find_modify():
    global arr, del_count, N,M
    dr=[1,-1,0,0]
    dc=[0, 0, 1, -1]
    no_update=True
    v=[[False]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            # BFS
            if v[r][c] or arr[r][c]==0:
                continue
            tmp = [(r,c)]
            og_val = arr[r][c]
            no_adj = True
            while tmp:
                cur_r,cur_c = tmp.pop()
                v[cur_r][cur_c] = True
                arr[cur_r][cur_c] = 0
                del_count+=1
                for di in range(4):
                    nr, nc = cur_r + dr[di], cur_c + dc[di]
                    nc = (nc+M)%M
                    if 0<=nr<N and v[nr][nc]==False:
                        if og_val == arr[nr][nc]:
                            v[nr][nc]=True
                            no_adj=False
                            no_update=False
                            tmp.append((nr,nc))
            if no_adj:
                arr[r][c] = og_val
                del_count-=1
    return no_update

def rotate(x,d,k):
    global arr
    for idx in range(1,N):
        num = idx*x-1
        if num >= N:
            break
        if d:   # ccw
            arr[num] = arr[num][k:] + arr[num][:k]
        else:   # cw
            arr[num] = arr[num][-k:] + arr[num][:-k]

def pm():
    global arr
    for l in arr:
        for e in l:
            print(e,end=' ')
        print()
    print("*--------------*")


N,M,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cmds= [list(map(int,input().split())) for _ in range(T)]
del_count=0    # 삭제된 숫자 개수 count

print(solution())