def solution():

    # Input
    N,M,K = map(int,input().split())
    A=[]
    for _ in range(N):
        A.append(list(map(int,input().split())))

    # Dice
    dice_front = [2,1,5,6]
    dice_side = [4,1,3,6]
    dice_di = 3-1
    dice_r, dice_c = 0, 0
    dr=[0,1,0,-1]   #1 ++는 시계방향 회전
    dc=[1,0,-1,0]   #2 +2는 반대방향 회전
    total_score = 0

    # MOVE
    for _ in range(K):
        # dice 위치 이동
        ndr, ndc = dice_r + dr[dice_di], dice_c + dc[dice_di]
        if ndr<0 or ndr>=N or ndc<0 or ndc>=M:
            dice_di = (dice_di+2)%4    #TODO 방향 잘 바뀌는지 Check
            ndr, ndc = dice_r + dr[dice_di], dice_c + dc[dice_di]
        dice_r,dice_c = ndr,ndc

        #TODO sanity check
        # dice 면 이동
        if dice_di==0:  # right
            dice_side = [dice_side[-1]]+dice_side[:-1]
            dice_front[1] = dice_side[1]
            dice_front[3] = dice_side[3]
        elif dice_di==1:    # down
            dice_front = [dice_front[-1]]+dice_front[:-1]
            dice_side[1] = dice_front[1]
            dice_side[3] = dice_front[3]
        elif dice_di==2:    # left
            dice_side = dice_side[1:] + [dice_side[0]]
            dice_front[1] = dice_side[1]
            dice_front[3] = dice_side[3]
        elif dice_di==3:    # up
            dice_front = dice_front[1:] + [dice_front[0]]
            dice_side[1] = dice_front[1]
            dice_side[3] = dice_front[3]
        else:
            raise Exception("in dice movement - dice_di")

        # Score - BFS
        B = A[dice_r][dice_c]
        C = 1
        dq=[(dice_r,dice_c)]
        visit = [[0]*M for _ in range(N)]
        visit[dice_r][dice_c] = 1
        while dq:   #TODO sanity check
            tmp_r, tmp_c = dq.pop()
            for tmp_di in range(4):
                tmp_nr, tmp_nc = tmp_r+dr[tmp_di], tmp_c+dc[tmp_di]
                if 0<=tmp_nr<N and 0<=tmp_nc<M:
                    if A[tmp_nr][tmp_nc]==B and visit[tmp_nr][tmp_nc] == 0:
                        visit[tmp_nr][tmp_nc] = 1
                        dq.append((tmp_nr,tmp_nc))
                        C+=1
        total_score += B*C

        # next dice_di
        bottom_num = dice_front[-1]
        if bottom_num!=dice_side[-1]:
            raise Exception("dice num update error")
        if bottom_num > B:
            dice_di = (dice_di+1)%4     # clock wise
        elif bottom_num < B:
            dice_di = (dice_di-1 + 4)%4 # ccw
        else:
            continue

    return total_score

T=int(input())
ans=[]
for _ in range(T):
    ans.append(solution())
for t in range(1,T+1):
    print(f"#{t} {ans[t-1]}")

"""
8
4 5 1
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
4 5 2
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
4 5 3
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
4 5 4
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
4 5 5
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
4 5 6
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
4 5 7
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
4 5 1000
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
"""