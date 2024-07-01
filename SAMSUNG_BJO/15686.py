def shortest_distance_M(idx_arr, prev_idx):
    global min_dist, dist_arr, M
    if len(idx_arr)==M:
        return
    for idx in range(prev_idx+1, len(dist_arr[0])):
        idx_arr.append(idx)
        calc_whole_dist(idx_arr)
        shortest_distance_M(idx_arr, idx)
        idx_arr.pop()

def calc_whole_dist(idx_arr):
    global min_dist, dist_arr
    total_dist = 0
    for h_idx in range(len(dist_arr)):
        home_min = 100000
        for c_idx in idx_arr:
            home_min = min(home_min, dist_arr[h_idx][c_idx])
        total_dist += home_min
    min_dist = min(total_dist, min_dist)


N,M = map(int,input().split())
h_arr=[]
c_arr=[]
for r in range(N):
    for c, ele in enumerate(map(int,input().split())):
        if ele==1:
            h_arr.append((r, c))
        elif ele==2:
            c_arr.append((r, c))
dist_arr = [[0] * len(c_arr) for _ in range(len(h_arr))]
for hi in range(len(h_arr)):
    for ci in range(len(c_arr)):
        hr, hc = h_arr[hi]
        cr, cc = c_arr[ci]
        dist_arr[hi][ci] = abs(hr - cr) + abs(hc - cc)
min_dist=1000000000
shortest_distance_M([], -1)
print(min_dist)