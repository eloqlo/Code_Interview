def solution():
    global tree_dict,K
    for debug_year in range(K):  #O(6000)
        tree_count = fall_winter(*spring_summer())
    print(tree_count)

def spring_summer():  #O(1000)
    global tree_dict, nut_arr
    fall_grow_pos = {}
    count = 0   # 살은 tree 개수
    for r,c in tree_dict.keys():
        rc_survived_trees = []
        rc_cur_trees = tree_dict[(r,c)]
        still_spring=True
        for age_idx in range(len(rc_cur_trees)):
            age = rc_cur_trees[age_idx]
            if age <= nut_arr[r][c] and still_spring:    # spring
                nut_arr[r][c] -= age
                rc_survived_trees.append(age+1)
                if (age+1)%5 == 0:
                    if (r,c) not in fall_grow_pos:
                        fall_grow_pos[(r,c)] = 1
                    else:
                        fall_grow_pos[(r,c)] += 1
            else:
                still_spring=False
                nut_arr[r][c] += age//2     # summer
        count += len(rc_survived_trees)
        tree_dict[(r,c)] = rc_survived_trees
    return count, fall_grow_pos

def fall_winter(count, fall_grow_pos):   #O(800+100)
    global tree_dict, nut_arr, plus_arr, N
    dr=[0,0,1,1,1,-1,-1,-1]
    dc=[1,-1,0,-1,1,1,0,-1]
    for r,c in fall_grow_pos.keys():
        for di in range(8):
            nr = r+dr[di]
            nc = c+dc[di]
            if 0<=nr<=N-1 and 0<=nc<=N-1:
                count += fall_grow_pos[(r,c)]
                if (nr,nc) not in tree_dict:
                    tree_dict[(nr,nc)] = [1]*fall_grow_pos[(r,c)]
                else:
                    tree_dict[(nr,nc)] = [1]*fall_grow_pos[(r,c)] + tree_dict[(nr,nc)]
    for r in range(N):
        for c in range(N):
            nut_arr[r][c] += plus_arr[r][c]
    return count


N, M, K = map(int,input().split())
plus_arr = []
for _ in range(N):
    plus_arr.append(list(map(int, input().split())))
tree_dict={}
for _ in range(M):
    r,c,a = map(int, input().split())
    tree_dict[(r-1,c-1)]=[a]
nut_arr=[[5]*N for _ in range(N)]
solution()