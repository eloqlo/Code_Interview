N,M = map(int, input().split())
num_map=[[0]*(M+2)]
for _ in range(N):
    num_map.append([0] + list(map(int,input().split())) +[0])
num_map += [[0]*(M+2)]

max_num= max(map(max,num_map))
result=0


def dfs(i, j, count, checked_locations):
    global result, num_map, N, M
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    tot = 0
    for i1, j1 in checked_locations:
        tot += num_map[i1][j1]
    if tot + max_num*(count) < result:
        return


    if count == 0:
        final_value=0
        for (final_i, final_j) in checked_locations:
            final_value += num_map[final_i][final_j]
        result = max(final_value, result)
        return

    # check special cases witch can't be solved by DFS.
    if count == 2:
        pp=[] # possible_positions
        for mv_idx in range(4):
            pp.append((i+di[mv_idx], j+dj[mv_idx]))
        pp.remove(checked_locations[0])
        root_value = num_map[checked_locations[0][0]][checked_locations[0][1]] + num_map[i][j]
        val0 = num_map[pp[0][0]][pp[0][1]]
        val1 = num_map[pp[1][0]][pp[1][1]]
        val2 = num_map[pp[2][0]][pp[2][1]]
        if val0!=0 and val1!=0:
            result = max(result, root_value + val0 + val1)
        if val1!=0 and val2!=0:
            result = max(result, root_value + val1 + val2)
        if val0!=0 and val2!=0:
            result = max(result, root_value + val0 + val2)


    for mv_idx in range(4):
        new_i = i + di[mv_idx]
        new_j = j + dj[mv_idx]

        condition1 = (1 <= new_i <= N)
        condition2 = (1 <= new_j <= M)
        condition3 = ((new_i, new_j) not in checked_locations)

        if condition1 and condition2 and condition3:
            dfs(new_i, new_j, count-1, checked_locations + [(new_i, new_j)])


def set_resultue():
    global count_flag
    # for every (ki,j) in num_map  -> O(10,000,000)
    for i in range(1,N+1):
        for j in range(1,M+1):
            dfs(i,j,3,[(i,j)])
            count_flag=False


set_resultue()
print(result)
