def solution():
    global shark_pos, arr, N, shark_size, total_time

    for _ in range(N*N):
        update_result = update_arr()
        # print_arr(total_time)
        if update_result == False:
            break
    return total_time

def print_arr(t):
    global arr, shark_pos, shark_size
    na = [l.copy() for l in arr]
    na[shark_pos[0]][shark_pos[1]] = f'({shark_size})'

    print(f"______{t}______")
    for line in na:
        for ele in line:
            print(ele, end='\t')
        print()
    print("_____________")


def update_arr():
    """
    arr: 원본 지도
    shark_pos: 상어 위치
    shark_size: 상어 크기
    total_time: 현재까지 시간
    """

    global arr, shark_pos, N, shark_size, total_time, kill_count
    chk=[[0]*N for _ in range(N)]
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]

    # 현재 상어가 먹을 수 있는 물고기 찾기
    q = [shark_pos]
    chk[shark_pos[0]][shark_pos[1]] = 1
    for t in range(1, 20*20+1):
        nxt_q = []
        edible = []
        while q:
            r,c = q.pop()
            for di in range(4):
                nr,nc = r+dr[di],c+dc[di]
                if 0<=nr<N and 0<=nc<N:
                    # 안 가봤다 / 갈 수 있다
                    if chk[nr][nc]==0 and arr[nr][nc] <= shark_size:
                        # 먹기, 지나가기
                        if arr[nr][nc]>0 and arr[nr][nc] < shark_size:
                            chk[nr][nc] = 1
                            edible.append((nr,nc))
                        elif arr[nr][nc]==0 or arr[nr][nc]==shark_size:
                            nxt_q.append((nr,nc))
                            chk[nr][nc]=1
        q = nxt_q
        if edible:
            break
        if not nxt_q:
            return False     # 갈곳X, 엄마상어 호출

    if not edible:
        raise Exception("ERR: 먹을 수 있는 물고기 없는데 다 탐색 안하고 끝난듯/nxt_q 조사")

    # 상어가 먹을 물고기 찾기
    if len(edible) == 1:
        shark_pos = edible[0]
    else:
        nr,nc = sorted(edible, key=lambda x: (x[0],x[1]))[0]
        shark_pos = nr,nc
    arr[shark_pos[0]][shark_pos[1]] = 0
    kill_count += 1
    total_time += t
    if kill_count == shark_size:
        shark_size += 1
        kill_count=0

    return True


N = int(input())
arr = []
shark_pos = None
shark_size = 2
total_time = 0
kill_count = 0
for r in range(N):
    nl=[]
    for c, foo in enumerate(map(int, input().split())):
        nl.append(foo)
        if foo == 9:
            shark_pos = (r,c)
            nl.pop()
            nl.append(0)
    arr.append(nl)

ans = solution()
print(ans)