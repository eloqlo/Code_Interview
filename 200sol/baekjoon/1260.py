from os import link
import sys
from collections import deque

n,m,v = map(int, sys.stdin.readline().strip().split())

graph=[]
for _ in range(m):
    x,y = map(int, sys.stdin.readline().strip().split())
    graph.append((x,y))

dfs_results = []
dfs_path= [False]*n
# stack구조, recursive로 작성
def dfs(v):
    dfs_path[v-1]=True
    dfs_results.append(v)
    
    linked_nodes_v = []
    for line in graph:
        if line[0]==v:
            linked_nodes_v.append(line[1])
        elif line[1]==v:
            linked_nodes_v.append(line[0])
    linked_nodes_v.sort()
    
    for node in linked_nodes_v:
        if not dfs_path[node-1]:
            dfs(node)
    
    return dfs_results


def bfs(v):
    bfs_path=[False]*n
    bfs_results=[]
    queue = deque()
    queue.append(v)
    bfs_path[v-1] = True
    
    while queue:
        vv = queue.popleft()
        bfs_results.append(vv)
        
        # 특정 노드랑 연관된 애들 내림차순 정리
        linked_nodes_v = []
        for line in graph:
            if line[0]==vv:
                linked_nodes_v.append(line[1])
            elif line[1]==vv:
                linked_nodes_v.append(line[0])
        linked_nodes_v.sort()
        
        for node in linked_nodes_v:
            if not bfs_path[node-1]:
                queue.append(node)
                bfs_path[node-1] = True
    
    return bfs_results
        

for i in dfs(v):
    print(i, end=' ')
print()
for i in bfs(v):
    print(i, end=' ')
print()