def dfs(dice_idx, score, possible_loc, finished_count):
    global dice, board, max_score
    if dice_idx == 10 or finished_count == 4:
        max_score = max(max_score,score)
        return
    if (len(possible_loc) < 4-finished_count) and ((0, 0) not in possible_loc):
        dfs(dice_idx, score, possible_loc + [(0,0)], finished_count)
        return
    for cur_x, cur_y in possible_loc.copy():
        possible_loc.remove((cur_x,cur_y))
        nx,ny = get_next_location(dice[dice_idx], cur_x, cur_y)

        if board[nx][ny] == -1:
            dfs(dice_idx + 1, score, possible_loc, finished_count + 1)
        elif (nx,ny) not in possible_loc:
            if type(board[nx][ny]) == tuple:
                dfs(dice_idx + 1, score + board[nx][ny][0], possible_loc + [(nx,ny)], finished_count)
            else:
                dfs(dice_idx + 1, score + board[nx][ny], possible_loc + [(nx,ny)], finished_count)
        possible_loc.append((cur_x,cur_y))

def get_next_location(dice_num, og_x, og_y):
    global board
    nx, ny = og_x, og_y
    if og_y == len(board[og_x])-1:
        nx = board[nx][ny][1]
        ny=0
    else:
        ny+=1
    dice_num-=1
    while dice_num:
        if board[nx][ny] == -1:
            break
        elif type(board[nx][ny])==tuple:
            nx = board[nx][ny][2]
            ny = 0
        else:
            ny += 1
        dice_num -= 1
    return nx, ny

dice = list(map(int,input().split()))
board = [[0,2,4,6,8,(10,1,2,True)],
         [13,16,(19,6,6,False)],
         [12,14,16,18,(20,3,4,True)],
         [22,(24,6,6,False)],
         [22,24,26,28,(30,5,7,True)],
         [28,27,(26,6,6,False)],
         [25,30,(35,8,8,False)],
         [32,34,36,(38,8,8,False)],
         [(40,9,9,False)],
         [-1]]
max_score = 0

dfs(0, 0, [], 0)
print(max_score)
