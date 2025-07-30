# INPUTS
n,m = map(int,input().split())
graph = {}
visit = set()
for nd in range(n+1):
    graph[nd] = []

for _ in range(m):
    u,v = map(int, input().split())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)
    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)

def dfs(nd):
    for ele in graph[nd]:
        if ele not in visit:
            visit.add(ele)
            dfs(ele)

cnt = 0
for nd in range(1, n+1):
    if nd not in visit:
        visit.add(nd)
        cnt += 1
        dfs(nd)

print(cnt)