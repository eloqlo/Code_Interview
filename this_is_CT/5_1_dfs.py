"""
p134 - dfs, bfs
"""

"""
adjacent list, matrix
"""
g =  [[] for _ in range(3)]    # 행이 3개인 2차원 리스트로 adjacent list 표현

# node 0, (#node, distance)
g[0].append((1,7))
g[0].append((2,5))

# node 1
g[1].append((0,7))

# node 2
g[2].append((0,5))

print(g)

"""
dfs - recursive
"""
def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],         # node 0 없음 이런 노드.
    [2,3,8],    # node 1
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드들 방문된 정보 1차원 리스트로 표현
visited = [False] * 9

dfs(graph, 1, visited)