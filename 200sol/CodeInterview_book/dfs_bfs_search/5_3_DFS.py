import sys

n,m = map(int, sys.stdin.readline().strip().split())

# 2차원 리스트 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# dfs로 특정 노드 방문한 뒤 연결된 모든 노드들 방문
def dfs(x, y):
    # 주어진 범위 벗어나면 즉시 종료
    if x<= -1 or x>=n or y <= -1 or y >= m:
        return False
    # 현재 노드 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] =1
        
        # 상하좌우 방문
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs수행
        if dfs(i,j) == True:
            result += 1

print(result)