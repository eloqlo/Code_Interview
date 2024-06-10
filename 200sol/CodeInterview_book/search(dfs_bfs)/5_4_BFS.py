"""
bfs의, queue처럼 주변 노드들을 탐색하는 느낌 알게됨.
벽이 0, 길이 1이기에 이렇게 짤 수 있던거.

bfs는 한 level씩 내려가기에, 이런 최단거리처럼 한칸씩 갔을 때, 제일 빨리 도달하는놈을 측정할 때 아주 어울리기에, 저자가 bfs가 이 문제에 아주 효과적이라 말한 것 같다.
"""
from collections import deque

n,m = map(int, input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int, input())))
    
# 이동할 방향 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때 까지 반복
    while queue:
        x, y = queue.popleft()
        # 현 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 1미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or nx>=n or y<0 or ny>=m:
                continue
            # 2벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 3해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    for i in range(len(graph)):
        print(graph[i])
    return graph[n-1][m-1]

# bfs를 수행한 결과 출력
print(bfs(0,0))