def solution():
    global glb_kill_count, glb_shark_size, glb_N
    count = 0
    for _i in range(glb_N**2):
        # next_time = func1()
        next_time = func2()
        if next_time == -1:
            break
        else:
            count += next_time
            glb_kill_count += 1
            if glb_kill_count == glb_shark_size:
                glb_shark_size += 1
                glb_kill_count = 0
    return count

def print_map(arr, time, r,c):
    print(f"------{time}------")
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==r and j==c:
                print("*", end=' ')
                continue
            if arr[i][j]==500:
                print("■", end=' ')
            else:
                print(arr[i][j], end=' ')
        print()
    print("--------------")
    print()

def func1():
    """
    update - map, global shark position
    return - end timestamp
    """
    global glb_shark_size, glb_shark_pos_r, glb_shark_pos_c, glb_map, glb_N
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    copy_map = [line.copy() for line in glb_map]
    cur_shark_pos = [(glb_shark_pos_r, glb_shark_pos_c)]
    fish_pos = []
    min_r = 100
    end_search = False
    end_timestamp = 0
    for cur_timestamp in range(glb_N**2):
        next_shark_pos = set()
        for r,c in cur_shark_pos:
            # found edible fish.
            if (1 <= copy_map[r][c] <= 6) and (copy_map[r][c] < glb_shark_size):
                fish_pos.append((r,c))
                min_r = min(r,min_r)
                end_search = True
                end_timestamp = cur_timestamp
                continue
            copy_map[r][c] = 500  # visited
            # 다음 갈 수 있는 곳 큐에 담기
            for di in range(4):
                nr = r + dr[di]
                nc = c + dc[di]
                if 0 <= nr < glb_N and 0 <= nc < glb_N:
                    if 0 <= copy_map[nr][nc] <= glb_shark_size:
                        next_shark_pos.add((nr,nc))
        cur_shark_pos = list(next_shark_pos)
        if end_search:
            break
        if len(cur_shark_pos) == 0:
            break

    if len(fish_pos) == 0:
        return -1

    # update map, global_shark_position.
    glb_map[glb_shark_pos_r][glb_shark_pos_c] = 0   # update global map 1
    min_r_idx_arr = []
    for idx, (r,c) in enumerate(fish_pos):
        if r == min_r:
            min_r_idx_arr.append(idx)
    min_c = 100
    final_idx = -1
    for idx in min_r_idx_arr:
        r,c = fish_pos[idx]
        if c < min_c:
            min_c = c
            final_idx = idx
    glb_shark_pos_r, glb_shark_pos_c = fish_pos[final_idx]  # update global shark position
    glb_map[glb_shark_pos_r][glb_shark_pos_c] = 9   # update global map 2
    return end_timestamp


def func2():
    """
    visited 따로 사용한다.

    update - map, global shark position
    return - end timestamp
    """
    global glb_shark_size, glb_shark_pos_r, glb_shark_pos_c, glb_map, glb_N
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    copy_map = [line.copy() for line in glb_map]
    cur_shark_pos = [(glb_shark_pos_r, glb_shark_pos_c)]
    fish_pos = []
    min_r = 100
    end_search = False
    end_timestamp = 0
    for cur_timestamp in range(glb_N**2):
        next_shark_pos = set()
        for r,c in cur_shark_pos:
            # found edible fish.
            if (1 <= copy_map[r][c] <= 6) and (copy_map[r][c] < glb_shark_size):
                fish_pos.append((r, c))
                min_r = min(r, min_r)
                end_search = True
                end_timestamp = cur_timestamp
                continue
            copy_map[r][c] = 500  # visited
            # 다음 갈 수 있는 곳 큐에 담기
            for di in range(4):
                nr = r + dr[di]
                nc = c + dc[di]
                if 0 <= nr < glb_N and 0 <= nc < glb_N:
                    if 0 <= copy_map[nr][nc] <= glb_shark_size:
                        next_shark_pos.add((nr,nc))

        cur_shark_pos = list(next_shark_pos)
        if end_search:
            break
        if len(cur_shark_pos) == 0:
            break

    if len(fish_pos) == 0:
        return -1

    # update map, global_shark_position.
    glb_map[glb_shark_pos_r][glb_shark_pos_c] = 0   # update global map 1
    min_r_idx_arr = []
    for idx, (r,c) in enumerate(fish_pos):
        if r == min_r:
            min_r_idx_arr.append(idx)
    min_c = 100
    final_idx = -1
    for idx in min_r_idx_arr:
        r,c = fish_pos[idx]
        if c < min_c:
            min_c = c
            final_idx = idx
    glb_shark_pos_r, glb_shark_pos_c = fish_pos[final_idx]  # update global shark position
    glb_map[glb_shark_pos_r][glb_shark_pos_c] = 9   # update global map 2
    return end_timestamp


# 백준용
glb_shark_size = 2
glb_shark_pos_r = 100
glb_shark_pos_c = 100
glb_kill_count = 0
glb_N = int(input())
glb_map = []
for r in range(glb_N):
    tmp = []
    for c, val in enumerate(map(int, input().split())):
        if val == 9:
            glb_shark_pos_r = r
            glb_shark_pos_c = c
        tmp.append(val)
    glb_map.append(tmp)


print(solution())