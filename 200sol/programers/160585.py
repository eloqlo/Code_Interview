def solution(board):
    count_o = 0
    count_x = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                count_o += 1
            elif board[i][j] == 'X':
                count_x += 1
    param_o_minus_x = count_o - count_x
    param_is_won, param_won_team = get_won_param(board)

    # consider error situation
    if param_o_minus_x not in [0, 1]:
        return 0
    elif param_is_won:
        if param_won_team == 'O' and param_o_minus_x != 1:
            return 0
        elif param_won_team == 'X' and param_o_minus_x != 0:
            return 0
    return 1


def get_won_param(board):
    """
    return True / False
    """
    # row
    for line in board:
        if line == 'OOO':
            return True, 'O'
        elif line == 'XXX':
            return True, 'X'

    # col
    for i in range(3):
        line = board[0][i] + board[1][i] + board[2][i]  # ! ERR CHK
        if line == 'OOO':
            return True, 'O'
        elif line == 'XXX':
            return True, 'X'

    # / or \
    lines = []
    lines.append(board[0][0] + board[1][1] + board[2][2])  # ! ERR CHK
    lines.append(board[2][0] + board[1][1] + board[0][2])  # ! ERR CHK
    for line in lines:
        if line == 'OOO':
            return True, 'O'
        elif line == 'XXX':
            return True, 'X'

    return False, None
