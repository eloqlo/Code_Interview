# INPUTS
N = int(input())
board=[]
for _ in range(N):
    board.append(list(map(int,input().split())))

max_value=0

def rotate_90(board):
    final_board=[]
    for rotated_line in zip(*board):
        new_rotated_line=[]
        for idx in range(len(rotated_line)-1,-1,-1):
            new_rotated_line.append(rotated_line[idx])
        final_board.append(new_rotated_line)
    return final_board

def rotate_minus90(board):
    reversed_board=[]
    final_board = []
    N = len(board)
    # reverse order
    for line in board:
        reversed_line=[]
        for idx in range(N-1, -1, -1):
            reversed_line.append(line[idx])
        reversed_board.append(reversed_line)
    # diagonal flip
    for rotated_line in zip(*reversed_board):
        final_board.append(list(rotated_line))
    return final_board

# move board into given position, return board.
def move_board(board, pos):
    # left <<
    if pos==0:
        final_board=[]
        for line in board:
            new_line=[]
            final_line=[]
            #1 move all elements to left side. | O(10)
            for ele in line:
                if ele==0:
                    continue
                else:
                    new_line.append(ele)
            new_line += [0 for _ in range(len(line)-len(new_line))]     #TODO sanity eheck
            #2 combine elements. | O(9)
            pass_next = False
            for idx in range(len(new_line)):
                if pass_next:
                    pass_next=False
                    continue
                # 합체 가능
                if idx<len(new_line)-1:
                    if new_line[idx] == new_line[idx+1]:
                        final_line.append(new_line[idx]*2)
                        pass_next=True
                        continue
                final_line.append(new_line[idx])
            final_line += [0 for _ in range(len(line)-len(final_line))]
            final_board.append(final_line)

    # right >>
    if pos == 1:
        final_board = []
        for line in board:
            right_line = []
            new_line = []

            final_line = []

            # 0 make items shift (left-right)
            for idx in range(len(line)-1,-1,-1):
                right_line.append(line[idx])

            # 1 move all elements to left side. | O(10)
            for ele in right_line:
                if ele == 0:
                    continue
                else:
                    new_line.append(ele)
            new_line += [0 for _ in range(len(line) - len(new_line))]

            # 2 combine elements. | O(9)
            pass_next = False
            for idx in range(len(new_line)):
                if pass_next:
                    pass_next = False
                    continue
                # 합체 가능
                if idx < len(new_line) - 1:
                    if new_line[idx] == new_line[idx + 1]:
                        final_line.append(new_line[idx] * 2)
                        pass_next = True
                        continue
                final_line.append(new_line[idx])
            final_line += [0 for _ in range(len(line) - len(final_line))]

            # make items shift again
            tmp_line=[]
            for idx in range(len(line) - 1, -1, -1):
                tmp_line.append(final_line[idx])
            final_line = tmp_line
            final_board.append(final_line)

    # move up: rotate-90 >> left move >> rotate90
    if pos==2:
        # rotate -90
        board_rotated_minus_90 = rotate_minus90(board)
        # same left move
        final_board = []
        for line in board_rotated_minus_90:
            new_line = []
            final_line = []
            # 1 move all elements to left side. | O(10)
            for ele in line:
                if ele == 0:
                    continue
                else:
                    new_line.append(ele)
            new_line += [0 for _ in range(len(line) - len(new_line))]  # TODO sanity eheck
            # 2 combine elements. | O(9)
            pass_next = False
            for idx in range(len(new_line)):
                if pass_next:
                    pass_next = False
                    continue
                # 합체 가능
                if idx < len(new_line)-1:
                    if new_line[idx] == new_line[idx + 1]:
                        final_line.append(new_line[idx] * 2)
                        pass_next = True
                        continue
                final_line.append(new_line[idx])
            final_line += [0 for _ in range(len(line) - len(final_line))]
            final_board.append(final_line)
        # rotate +90
        final_board = rotate_90(final_board)

    # down
    if pos==3:
        # rotate +90
        board = rotate_90(board)

        # same left move
        final_board = []
        for line in board:
            new_line = []
            final_line = []
            # 1 move all elements to left side. | O(10)
            for ele in line:
                if ele == 0:
                    continue
                else:
                    new_line.append(ele)
            new_line += [0 for _ in range(len(line) - len(new_line))]  # TODO sanity eheck
            # 2 combine elements. | O(9)
            pass_next = False
            for idx in range(len(new_line)):
                if pass_next:
                    pass_next = False
                    continue
                # 합체 가능
                if idx < len(new_line)-1:
                    if new_line[idx] == new_line[idx + 1]:
                        final_line.append(new_line[idx] * 2)
                        pass_next = True
                        continue
                final_line.append(new_line[idx])
            final_line += [0 for _ in range(len(line) - len(final_line))]
            final_board.append(final_line)
        # rotate -90
        final_board = rotate_minus90(final_board)

    return final_board

def calc_max_value(board):
    max_val=0
    for line in board:
        max_val = max(max_val, max(line))
    return max_val

# one board --> 4 results into list.
def move_board_list(board):
    global max_value

    result=[]
    # 4 directions
    for pos in range(4):
        moved_board = move_board(board, pos)
        unchanged=True
        # TODO: possible hazard !
        for mline, line in zip(moved_board,board):
            if mline != line:
                unchanged = False
        if unchanged:
            max_value=max(max_value, calc_max_value(moved_board))
        else:
            result.append(moved_board)

    # result: [board1, board2, board3, board4]
    return result

def solution(board):
    global max_value
    queue = [board]

    # calculate 5 possible times
    for t in range(5):
        tmp_queue = []
        for cur_board in queue:
            moved_board_list = move_board_list(cur_board)
            tmp_queue += moved_board_list
        queue = tmp_queue

    # calculate max value
    for finished_board in queue:
        max_val = calc_max_value(finished_board)
        max_value = max(max_val, max_value)

    return max_value

print(solution(board))