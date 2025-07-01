############################################
################## INPUTS ##################
N = int(input())
K = int(input())

board = []
for i in range(N+2):
    if i==0 or i==N+1:
        board.append(["#"]*(N+2))
    elif i==1:
        line = ['.'] * (N+2)
        line[0] = '#'
        line[-1] = '#'
        line[1] = 'S'
        board.append(line)
    else:
        line = ['.']*(N+2)
        line[0]='#'
        line[-1]='#'
        board.append(line)

apple_pos=[]
for _ in range(K):
    y,x = map(int, input().split())
    apple_pos.append((y,x))
    board[y][x]="A"

commands={"time":[],"command":[]}
L = int(input())
for _ in range(L):
    X,C = input().split()
    commands["time"].append(int(X))
    commands["command"].append(C)

snake=[(1,1)]


################# FUNCTIONS ################
def print_board(board, t):
    global snake
    print()
    print(f"______________ time : {t} _______________")
    for line in board:
        for ele in line:
            print(f"{ele} ", end='')
        print()
    print()

    print("snake - ",snake)

# def rotate_board_L(board):
#     global snake, N
#     final_board=[]
#     dig_board=[]
#     fliped_board=[]
#     final_snake=[]
#
#     # modify board: 반전 -> 대각화 -> 반전
#     for line in board:
#         fliped_board.append([line[idx] for idx in range(len(line)-1,-1,-1)])
#     for line in zip(*fliped_board):
#         dig_board.append(list(line))
#     for line in dig_board:
#         final_board.append([line[idx] for idx in range(len(line) - 1, -1, -1)])
#
#     # SANITY CHECK !
#     # final_board2=[]
#     # fliped_board2=[]
#     # dig_board2=[]
#     # for line in final_board:
#     #     fliped_board2.append([line[idx] for idx in range(len(line)-1,-1,-1)])
#     # for line in zip(*fliped_board2):
#     #     dig_board2.append(list(line))
#     # for line in dig_board2:
#     #     final_board2.append([line[idx] for idx in range(len(line) - 1, -1, -1)])
#     #
#     # print("############################################")
#     # print_board(board, 0)
#     # print()
#     # print_board(final_board2, 1)
#     # print("############################################")
#
#     # failed..?
#     # new_board= [["X"]*(N+2) for _ in range(N+2)]
#     # for old_y in range(len(board)):
#     #     for old_x in range(len(board)):
#     #         new_y = N+1 - old_x
#     #         new_x = N+1 - old_y
#     #         new_board[new_y][new_x] = board[old_y][old_x]
#
#     # modify snake coordinate
#     for y,x in snake:
#         y_new = N+1 - x
#         x_new = N+1 - y
#         final_snake.append((y_new,x_new))
#     snake = final_snake
#     return final_board
#
# def rotate_board_D(board):
#     global snake, N
#     final_board = []
#     fliped_board = []
#     final_snake = []
#
#     # modify board: 반전 -> 대각화
#     for line in board:
#         fliped_board.append([line[idx] for idx in range(len(line) - 1, -1, -1)])
#     for dig_line in zip(*fliped_board):
#         final_board.append(list(dig_line))
#
#     # modify snake coordinate
#     for y, x in snake:
#         y_new = N + 1 - x   #TODO sanity check
#         x_new = y
#         final_snake.append((y_new, x_new))
#         # sanity check
#         if final_board[y_new][x_new] != "S":
#             print(final_board[y_new][x_new])
#             print('D flip, Snake position Erorr')
#             print(board)
#             print('snake: ', snake)
#             print('old coordL ', y, x)
#             print('new coord: ', y_new, x_new)
#             raise
#
#     snake = final_snake
#     return final_board

def get_next_board(board, t, d_idx):
    global commands, snake
    # ['right','down','left','up']
    dy=[0,1,0,-1]
    dx=[1,0,-1,0]

    next_board = []
    for idx in range(N + 2):
        next_board.append(board[idx].copy())

    is_end = False

    # check if it's time to rotate
    # move snake to right.
    snake_head = snake[0]
    if t - 1 in commands["time"]:
        idx = commands["time"].index(t - 1)
        req_command = commands["command"][idx]
        if req_command == "D":
            d_idx = (d_idx + 1) % 4
        elif req_command == "L":
            d_idx = (d_idx + 3) % 4

    nxt_x = snake_head[1] + dx[d_idx]
    nxt_y = snake_head[0] + dy[d_idx]
    if next_board[nxt_y][nxt_x] == "#":
        is_end=True
        return next_board, is_end, d_idx
    elif next_board[nxt_y][nxt_x] == "A":
        next_board[nxt_y][nxt_x] = "S"
        snake.insert(0,(nxt_y, nxt_x))
        return next_board, is_end, d_idx
    elif next_board[nxt_y][nxt_x] == "S":
        is_end = True
        return next_board, is_end, d_idx
    elif next_board[nxt_y][nxt_x] == ".":
        snake.insert(0,(nxt_y,nxt_x))
        next_board[nxt_y][nxt_x]= "S"
        tail_y=snake[-1][0]
        tail_x=snake[-1][1]
        next_board[tail_y][tail_x]= "."
        snake.pop()
        return next_board, is_end, d_idx
    else:
        "ERROR"
        raise


def solution(board):

    d_idx=0
    for t in range(1,int(1e+9)):
        board, is_end, d_idx = get_next_board(board, t, d_idx)
        # print_board(board,t)  #TODO debug..

        if is_end:
            break

    return t


if __name__=='__main__':
    print(solution(board))