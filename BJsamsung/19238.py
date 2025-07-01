def solution():
    n,m,fuel=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(n)]
    tr,tc=map(int,input().split())
    tr-=1; tc-=1
    passengers_from_goal={}
    for _ in range(m):
        sr, sc, gr, gc = map(int,input().split())
        sr, sc, gr, gc = sr-1, sc-1, gr-1, gc-1
        passengers_from_goal[(sr,sc)] = [gr,gc]
        board[sr][sc]='p'

    for idx in range(m):
        # print(f"{idx+1}째 승객, 현 연료 {fuel}")
        pr,pc,dist1 = nearest_passenger_loc_dist(board,tr,tc)
        if dist1 == -1 or fuel<dist1:
            return -1
        # print(f"{idx + 1}째 승객까지 거리 {dist1} / 승객위치 {pr,pc}/ 시작위치 {tr,tc}")
        fuel -= dist1
        gr,gc = passengers_from_goal[(pr,pc)]
        dist2 = find_short_route(board,pr,pc,gr,gc)
        if fuel<dist2 or dist2==-1:
            return -1
        board[pr][pc]=0
        fuel -= dist2
        fuel += dist2 * 2
        tr,tc = gr,gc
        # print(f"{idx + 1}째 승객 목적지 까지 거리 {dist2}")
        # print(f"남은 연료 {fuel}")
        # print()

    return fuel
def pm(b):
    for l in b:
        for e in l:
            print(e, end=' ')
        print()
    print()

def nearest_passenger_loc_dist(board,tr,tc):
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    cur_pos = [(tr,tc)]
    end_pos = []
    end_flag = False
    dist = -1
    visit = [[0]*len(board) for _ in range(len(board))]
    if board[tr][tc]=='p':
        return tr,tc,0
    while cur_pos and (not end_flag):
        dist += 1
        nxt_pos = []
        for r,c in cur_pos:
            visit[r][c] = 1
            for di in range(4):
                nr,nc = r+dr[di], c+dc[di]
                if 0<=nr<=len(board)-1 and 0<=nc<=len(board)-1:
                    if board[nr][nc]=='p' and visit[nr][nc]==0:
                        end_flag=True
                        end_pos.append((nr, nc))
                        visit[nr][nc] = 1
                    elif board[nr][nc]==1:
                        continue
                    elif board[nr][nc]==0 and visit[nr][nc]==0:
                        nxt_pos.append((nr, nc))
                        visit[nr][nc] = 1
        cur_pos = nxt_pos
    if end_flag:
        dist+=1
    if len(end_pos)==0:
        return -1,-1,-1
    elif len(end_pos)==1:
        return end_pos[0][0], end_pos[0][1], dist
    else:
        nr,nc = sorted(end_pos, key=lambda x:(x[0],x[1]))[0]
        return nr, nc, dist


def find_short_route(board,tr,tc,gr,gc):
    dist=-1
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    cur_pos=[(tr,tc)]
    visit = [[0]*len(board) for _ in range(len(board))]
    while cur_pos:
        nxt_pos=[]
        dist += 1
        for r,c in cur_pos:
            if (r, c) == (gr, gc):
                return dist
            visit[r][c] = 1
            for di in range(4):
                nr,nc = r+dr[di], c+dc[di]
                if 0<=nr<=len(board)-1 and 0<=nc<=len(board)-1:
                    if (board[nr][nc]==0 or board[nr][nc]=='p') and visit[nr][nc]==0:
                        nxt_pos.append((nr,nc))
                        visit[nr][nc]=1
        cur_pos = nxt_pos
    return -1

print(solution())