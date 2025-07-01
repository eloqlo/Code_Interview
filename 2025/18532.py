import sys

def solution():
    N,M,K,X = map(int, input().split())
    graph = {}
    for _ in range(M):
        a,b = map(int, sys.stdin.readline().split())
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
    
    visit = set([X])
    dist = 0
    cur = [X]
    while cur:
        dist += 1
        nxt = []
        for node in cur:
            if node not in graph:
                continue
            for nxt_node in graph[node]:
                if nxt_node not in visit:
                    nxt.append(nxt_node)
                    visit.add(nxt_node)
        if dist == K:
            if nxt:
                return nxt
            else:
                return [-1]
        cur = nxt
    
    raise Exception("BFS ERROR")

ans = solution()
ans.sort()
print(ans)