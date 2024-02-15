# https://www.acmicpc.net/problem/18352

"""
bfs
"""
import sys
from collections import deque

N,M,K,X = map(int,input().split(' '))
road={node: [] for node in range(1,N+1)}
for _ in range(M):
    x1,x2=map(int,sys.stdin.readline().rstrip().split(' '))
    road[x1].append(x2)

if __name__=="__main__":
    q=deque()
    check=[-1 for _ in range(N+1)]
    q+=road[X]
    check[X]=0
    count=0
    
    while q:
        if count==K:
            break
        count+=1
        next_nodes=set()
        while q:
            cur_node=q.popleft()
            if check[cur_node]==-1:  # 아직 안간 도시면
                check[cur_node]=count   # 최단거리에 저장
                next_nodes.update(road[cur_node])  # 걔랑 이어진 곳 방문리스트에 추가
        q=deque(next_nodes)
    
    ans=[]
    for node, distance in enumerate(check):
        if distance==K:
            ans.append(node)
    ans.sort()
    
    if len(ans)>0:
        for node in ans:
            print(node)
    else:
        print(-1)