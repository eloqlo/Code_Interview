def print_arr(arr):
    # print arr_
    print()
    for line in arr:
        for ele in line:
            print(ele, end=' ')
        print()

def solution(idx, arr):
    global min_val, cctv_arr

    # copy
    arr_ = []
    for line in arr:
        arr_.append(line.copy())

    # 종결조건
    if idx == len(cctv_arr):
        # count 사각지대
        counter = 0
        for line in arr_:
            for ele in line:
                if ele == 0:
                    counter += 1
        min_val = min(min_val, counter)
        return

    # dfs
    for di in range(4):
        i,j = cctv_arr[idx]
        cv = arr_[i][j]     # cctv value
        if cv==2 and di==2:
            break
        if cv==5 and di==1:
            break
        new_arr = get_new_map(di, arr_, idx)     # 현재 direction, cctv_val 따라서 새로운 arr 만듦
        solution(idx+1, new_arr)

def east(arr, i,j):
    global M
    # 동
    if j < M - 1:
        for nj in range(j + 1, M):
            if arr[i][nj] == 0:
                arr[i][nj] = '#'
            elif arr[i][nj] != 6:
                continue
            else:
                # 벽
                break
    return arr
def west(arr, i,j):
    global M
    # 서
    if j > 0:
        for nj in range(j - 1, -1, -1):
            if arr[i][nj] == 0:
                arr[i][nj] = '#'
            elif arr[i][nj] != 6:
                continue
            else:
                # 벽
                break
    return arr
def south(arr,i,j):
    global N
    # 남
    if i < N - 1:
        for ni in range(i + 1, N):
            if arr[ni][j] == 0:
                arr[ni][j] = '#'
            elif arr[ni][j] != 6:
                continue
            else:
                # 벽
                break
    return arr
def north(arr,i,j):
    global N
    # 북
    if i>0:
        for ni in range(i - 1, -1, -1):
            if arr[ni][j] == 0:
                arr[ni][j] = '#'
            elif arr[ni][j] != 6:
                continue
            else:
                # 벽
                break
    return arr

def get_new_map(di, arr, idx):
    global cctv_arr, N, M

    cur_arr = []
    for line in arr:
        cur_arr.append(line.copy())

    i,j = cctv_arr[idx]
    cctv_type = cur_arr[i][j]

    if cctv_type == 1:
        if di==0:
            # 동
            new_arr = east(cur_arr,i,j)
        elif di==1:
            # 서
            new_arr = west(cur_arr,i,j)
        elif di==2:
            # 남
            new_arr = south(cur_arr, i, j)
        elif di==3:
            # 북
            new_arr = north(cur_arr, i, j)
    elif cctv_type == 2:
        # 가로
        if di==0:
            new_arr = east(cur_arr,i,j)
            new_arr = west(new_arr,i,j)
        # 세로
        elif di==1:
            new_arr = south(cur_arr,i,j)
            new_arr = north(new_arr,i,j)
        else:
            raise Exception("direction index error ! in get_new_map !")
    elif cctv_type == 3:
        if di==0:
            new_arr = north(cur_arr,i,j)
            new_arr = east(new_arr,i,j)
        elif di==1:
            new_arr = south(cur_arr, i, j)
            new_arr = east(new_arr, i, j)
        elif di==2:
            new_arr = south(cur_arr, i, j)
            new_arr = west(new_arr, i, j)
        elif di==3:
            new_arr = north(cur_arr, i, j)
            new_arr = west(new_arr, i, j)
    elif cctv_type == 4:
        if di == 0:
            new_arr = north(cur_arr, i, j)
            new_arr = east(new_arr, i, j)
            new_arr = south(new_arr,i,j)
        elif di == 1:
            new_arr = south(cur_arr, i, j)
            new_arr = east(new_arr, i, j)
            new_arr = west(new_arr, i, j)
        elif di == 2:
            new_arr = south(cur_arr, i, j)
            new_arr = west(new_arr, i, j)
            new_arr = north(new_arr, i, j)
        elif di == 3:
            new_arr = north(cur_arr, i, j)
            new_arr = west(new_arr, i, j)
            new_arr = east(new_arr, i, j)
    elif cctv_type == 5:
        new_arr = north(cur_arr, i, j)
        new_arr = west(new_arr, i, j)
        new_arr = east(new_arr, i, j)
        new_arr = south(new_arr, i, j)
    else:
        print("error: cctv_type error ", cctv_type)
        raise

    return new_arr


"""baekjun version output"""
N,M = map(int, input().split())
arr = []
cctv_arr=[]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if 0<line[j]<6:
            cctv_arr.append([i,j])
    arr.append(line)
min_val = 8*8

solution(0, arr)
print(min_val)


# """samsung version output"""
# K = int(input())
# outputs=[]
# for i in range(K):
#     N, M = map(int, input().split())
#     arr = []
#     cctv_arr = []
#     min_val = 8 * 8
#     for i in range(N):
#         line = list(map(int, input().split()))
#         for j in range(M):
#             if 0 < line[j] < 6:
#                 cctv_arr.append([i, j])
#         arr.append(line)
#     solution(0,arr)
#     outputs.append(min_val)
#
# for idx, output in enumerate(outputs):
#     print(f"#{idx+1} {output}")