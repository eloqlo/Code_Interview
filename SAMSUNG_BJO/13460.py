N,M = list(map(int,input().split()))
board=[]
ry, rx, by, bx = None,None,None,None
for y in range(N):
    arr=[s for s in input()]
    board.append(arr)
    for x in range(M):
        if arr[x]=='R':
            rx=x
            ry=y
        elif arr[x]=='B':
            bx=x
            by=y

def print_board(board, count):
    # for debugging
    print(f"___________ At count {count} ___________")
    for row in board:
        print(''.join(row))
    print("_________________________________________")

def bfs(board, ry,rx,by,bx):
    global N,M
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    queue=[[(ry,rx),(by,bx)]]
    visited=[[(ry,rx),(by,bx)]]

    #1 11번의 기울임
    for count in range(1,11):
        tmp_queue=[]
        #2 t시점의 위치들 받아온다.
        for rpos, bpos in queue:
            #3 t시점의 위치에서 한 방향씩 기울여 보고, 가능하면 t+1 queue에 저장한다.
            for di in range(4):
                rt=rpos
                bt=bpos

                #4 유효 횟수 8초
                for _ in range(8):
                    flagR=False
                    flagB=False
                    r_t1 = (rt[0]+dy[di], rt[1]+dx[di]) # next position
                    b_t1 = (bt[0]+dy[di], bt[1]+dx[di])

                    # blue가 O에 도달하는 경우면 pass 해버린다.
                    if board[b_t1[0]][b_t1[1]]=='O':
                        break

                    # update R -- 안 낑겼고, 벽 아니고.
                    if not (board[b_t1[0]][b_t1[1]]=='#' and r_t1==bt) and (board[r_t1[0]][r_t1[1]]!='#'):
                        # condition: finish
                        if board[r_t1[0]][r_t1[1]] == 'O':
                            finish_flag=True

                            # check if blue can go to 'O'
                            for idx in range(1,9):
                                check_b_y = max(1,min(N-2, bt[0] + dy[di]*idx))     #?
                                check_b_x = max(1,min(M-2, bt[1] + dx[di]*idx))     #?
                                if board[check_b_y][check_b_x]=='#':
                                    break
                                if board[check_b_y][check_b_x]=='O':
                                    finish_flag=False

                            if finish_flag:
                                return count
                            else:
                                break   # 이 방향은 아니다.
                        # move R
                        rt = r_t1
                        flagR = True

                    # update B
                    if board[b_t1[0]][b_t1[1]]!='#' and rt!=b_t1:
                        # move B
                        bt = b_t1
                        flagB = True

                    # 한 방향으로 더이상 안 움직인다.
                    if not (flagR or flagB):
                        # 도착지가 이미 조회한 곳이면 큐에 반영 X
                        if [(rt,bt)] in visited:
                            break
                        tmp_queue.append([rt,bt])
                        visited.append([(rt,bt)])
                        board[rt[0]][rt[1]]='R'
                        board[bt[0]][bt[1]]='B'

        # print_board(board,count)
        queue=tmp_queue

    return -1

answer = bfs(board, ry,rx,by,bx)

print(answer)