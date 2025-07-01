from collections import deque

def solution(board):
    N = len(board)
    # enlarge board for convenience.
    new_board = [[1]*(N+2)]
    for line in board:
        new_board.append([1] + line + [1])
    new_board.append([1] * (N + 2))
    cur_positions = deque()
    cur_positions.append((1,1,1,2))    # r1,c1, r2,c2
    visited = [line.copy() for line in new_board]
    for time in range(1000000):
        next_positions=set()
        while cur_positions:
            r1,c1,r2,c2 = cur_positions.popleft()
            visited[r1][c1] = visited[r2][c2] = "V"   # VISITED
            # 종료 조건
            if (r1,c1)==(N,N) or (r2,c2)==(N,N):
                return time
            # 안가본 위치 다음 갈곳에 담기
            next_positions = next_positions.union(get_next_possible_pos((r1,c1,r2,c2), visited))
        if len(next_positions)==0:
            raise Exception("not supposed to be")
        cur_positions = deque(next_positions)
    return None

def get_next_possible_pos(cur_pos, visited):
    """
    다음 될 수 있는 안가본 포지션들을 set로 return
    - 여기선 visit 수정하면 안돼!
    - 그냥 queue에 담아서 넘기기만 하면 된다.
    """

    print("----------")
    for line in visited:
        for ele in line:
            print(ele, end=' ')
        print()
    print("----------")

    N = len(visited)
    r1,c1,r2,c2 = cur_pos
    next_positions = set()
    #1 up
    nr1, nc1, nr2, nc2 = r1 - 1, c1, r2 - 1, c2
    if visited[nr1][nc1] != 1 and visited[nr2][nc2] != 1:   # 벽 체크
        if visited[nr1][nc1] != "V" or visited[nr2][nc2] != "V":    # 이전 방문 체크
            next_positions.add((nr1, nc1, nr2, nc2))
    # down
    nr1, nc1, nr2, nc2 = r1 + 1, c1, r2 + 1, c2
    if visited[nr1][nc1] != 1 and visited[nr2][nc2] != 1:   # 벽 체크
        if visited[nr1][nc1] != "V" or visited[nr2][nc2] != "V":    # 이전 방문 체크
            next_positions.add((nr1, nc1, nr2, nc2))
    # right
    nr1, nc1, nr2, nc2 = r1, c1+1, r2, c2+1
    if visited[nr1][nc1] != 1 and visited[nr2][nc2] != 1:  # 벽 체크
        if visited[nr1][nc1] != "V" or visited[nr2][nc2] != "V":  # 이전 방문 체크
            next_positions.add((nr1, nc1, nr2, nc2))
    # left
    nr1, nc1, nr2, nc2 = r1, c1 - 1, r2, c2 - 1
    if visited[nr1][nc1] != 1 and visited[nr2][nc2] != 1:  # 벽 체크
        if visited[nr1][nc1] != "V" or visited[nr2][nc2] != "V":  # 이전 방문 체크
            next_positions.add((nr1, nc1, nr2, nc2))
    # rotations
    if r1==r2:
        if visited[r2-1][c2]!=1 and visited[r1-1][c1]==0:
            next_positions.add((r1+1, c1, r2, c2-1))
        if visited[r2+1][c2]!=1 and visited[r1+1][c1]==0:
            next_positions.add((r1, c1, r2+1, c2-1))
        if visited[r1-1][c1]!=1 and visited[r2-1][c2]==0:
            next_positions.add((r1-1,c1+1,r2,c2))
        if visited[r1+1][c1]!=1 and visited[r2+1][c2]==0:
            next_positions.add((r1,c1+1,r2+1,c2))
    else:   # vertical
        if visited[r2][c2-1]!=1 and visited[r1][c1-1]==0:
            next_positions.add((r1, c1-1, r2-1, c2))
        if visited[r2][c2+1]!=1 and visited[r1][c1+1]==0:
            next_positions.add((r1, c1, r2-1, c2+1))
        if visited[r1][c1-1] != 1 and visited[r2][c2-1] == 0:
            next_positions.add((r1+1, c1-1, r2, c2))
        if visited[r1][c1+1] != 1 and visited[r2][c2+1] == 0:
            next_positions.add((r2,c2,r2,c2+1))

    return next_positions


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))