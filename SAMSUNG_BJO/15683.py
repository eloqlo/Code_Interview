def solution():
    global N,M,arr,cam_li

    dfs(0,[])

def dfs(idx, cam_di_li):
    global cam_li, arr
    if idx == len(cam_li):
        count_result_space(cam_di_li, arr)
        return

    now_cam, now_r, now_c = cam_li[idx]

    if now_cam == 2:
        dfs(idx + 1, cam_di_li + [0])
        dfs(idx + 1, cam_di_li + [1])
    elif now_cam == 5:
        dfs(idx + 1, cam_di_li + [0])
    elif now_cam == 1 or now_cam == 3 or now_cam == 4:
        dfs(idx + 1, cam_di_li + [0])
        dfs(idx + 1, cam_di_li + [1])
        dfs(idx + 1, cam_di_li + [2])
        dfs(idx + 1, cam_di_li + [3])
    else:
        raise


# 현재 cam_di_li 조합에 대한 사각지대 크기 계산
counter=0
def count_result_space(cam_di_li, arr):
    global cam_li, min_space, counter
    counter+=1
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    for cam_idx in range(len(cam_li)):
        di = cam_di_li[cam_idx]
        cam, r, c = cam_li[cam_idx]
        if cam == 1 or cam == 3 or cam == 4:
            for num in range(1,8+1):
                nr = r + dr[di]*num
                nc = c + dc[di]*num
                if 0 <= nr <= N - 1 and 0 <= nc <= M - 1:
                    if arr[nr][nc] == 6:
                        break
                    arr[nr][nc] = '#'
                else:
                    break
        elif cam == 2:
            if di==0:   # row
                for num in range(1, 8 + 1):
                    nr = r + dr[0] * num
                    nc = c + dc[0] * num
                    if 0 <= nr <= N - 1 and 0 <= nc <= M - 1:
                        if arr[nr][nc] == 6:
                            break
                        arr[nr][nc] = '#'
                    else:
                        break
                for num in range(1, 8 + 1):
                    nr = r + dr[1] * num
                    nc = c + dc[1] * num
                    if 0 <= nr <= N - 1 and 0 <= nc <= M - 1:
                        if arr[nr][nc] == 6:
                            break
                        arr[nr][nc] = '#'
                    else:
                        break
            elif di==1:  # col
                for num in range(1, 8 + 1):
                    nr = r + dr[2] * num
                    nc = c + dc[2] * num
                    if 0 <= nr <= N - 1 and 0 <= nc <= M - 1:
                        if arr[nr][nc] == 6:
                            break
                        arr[nr][nc] = '#'
                    else:
                        break
                for num in range(1, 8 + 1):
                    nr = r + dr[3] * num
                    nc = c + dc[3] * num
                    if 0 <= nr <= N - 1 and 0 <= nc <= M - 1:
                        if arr[nr][nc] == 6:
                            break
                        arr[nr][nc] = '#'
                    else:
                        break
        elif cam == 5:
            for di in range(4):
                for num in range(1, 8 + 1):
                    nr = r + dr[di] * num
                    nc = c + dc[di] * num
                    if 0 <= nr <= N - 1 and 0 <= nc <= M - 1:
                        if arr[nr][nc] == 6:
                            break
                        arr[nr][nc] = '#'
                    else:
                        break
        else:
            print("Error: count_result_space() - cam_li - cam")
            raise

    # count current remain space
    count=0
    for line in arr:
        for ele in arr:
            if ele==0:
                count+=1

    # DEBUG
    print(f"________ solution N.{counter} ________")
    for line in arr:
        for ele in arr:
            print(ele, end=" ")
        print()

    min_space = min(min_space, count)

if __name__=="__main__":
    results=[]
    T = int(input())
    for _ in range(T):
        N,M = map(int, input().split())
        arr = [[0]*M for _ in range(N)]
        cam_li = []
        min_space = 1000
        for r in range(N):
            for c, ele in enumerate(map(int, input().split())):
                arr[r][c] = ele
                if ele!=0 and ele!=6:
                    cam_li.append([ele,r,c])

        solution()
        results.append(min_space)

    for num in range(T):
        print(f"#{num+1} {results[num]}")