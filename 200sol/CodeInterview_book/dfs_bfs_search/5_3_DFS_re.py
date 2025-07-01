"""
이 얼음물 채우기는, 그저 연결된 노드들을 탐색하기만 하면 됐다. 따라서 dfs든 bfs이든 누구를 쓰든 상관이 없었을 것 이다.ㄴ
"""

"""
한 node를 찍으면 연관된 node들 다 탐색 stack 구조로.
"""
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().strip().split())

# 2차원 리스트 생성
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# main에서 모든 칸을 이거로 조회할거임. 그거 생각
# stack 구조가 맞지. 먼저 방문한애 위로 쌓이니깐
def dfs(x,y):
    # 영역 벗어났으면 False(바로 나옴)
    if x<0 or y<0 or x>n-1 or y>m-1:
        return False
    # 만일 미개척지면?
    if graph[x][y] == 0:
        graph[x][y] = 1   # 개척하고
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)  # 주위 다 채우기!
        return True # 주변 한뭉탱이들 채우고 True 반환.
    return False # 이미 개척된놈이면 False 반환(count x)

# 얘로도 똑같이 할 수 있는거 아닌가?
# 빈곳 찾으면 주변 다 칠해주는 애.
"""
count
for n,m
    if 빈공간이다?
    bfs() -> 연관된곳 다 칠하기.
    count+=1
return count
"""
# 이동할 방향 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 1미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or nx>=n or y<0 or ny>=m:
                continue
            # 이미 채워진경우 무시
            if graph[nx][ny]==1:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=1
                queue.append((nx,ny))
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            count += 1

print(count)