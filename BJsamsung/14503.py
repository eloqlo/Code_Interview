N,M = map(int, input().split())
r,c,d = map(int, input().split())
room_map=[]
for _ in range(N):
    room_map.append([ele for ele in map(int,input().split())])

def print_map(time):
    global room_map
    print(f"__________ at {time} ____________")
    for line in room_map:
        for ele in line:
            print(ele, end=' ')
        print()
    print("________________________________")

def solution():
    global N,M,r,c,d,room_map
    is_end=False
    result=0

    # 현위치 + drc[가고자 방향] = 다음위치
    # 붕 동 남 서
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while not is_end:
        
        # 현위치 청소
        if room_map[r][c] == 0:
            room_map[r][c] = "."
            result += 1
            # print_map(result)       # DEBUGGING

        # 4방향 중 이동가능 순서대로 찾기
        can_move = False
        for d_idx in range(4):
            # 위치 구하고
            nd = (4 + d - (d_idx+1)) % 4
            nr = r + dr[nd]
            nc = c + dc[nd]

            # 청소 가능 있으면 이동, next loop
            if room_map[nr][nc]==0:
                r,c = nr, nc
                d = nd
                can_move=True
                break

        # 갈데 없으면 후진
        if not can_move:

            # 뒷 방향 확인
            nd = (d+2)%4
            nr = r + dr[nd]
            nc = c + dc[nd]

            if room_map[nr][nc]==1:
                is_end=True
            else:
                r = nr
                c = nc

    print(result)

solution()