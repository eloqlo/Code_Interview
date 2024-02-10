import sys
from collections import deque

n,m=map(int,input().split())
l=[]
for _ in range(n):
    inp=input()
    l.append([int(k) for k in inp])
count=0

def fill(i_,j_):
    global l
    q=deque([(i_,j_)])
    
    while q:
        # queue에서 하나의 원소를 뽑아 방문처리
        i,j = q.popleft()
        l[i][j]=1
        
        # 해당 위치와 연결된 방문하지 않은 위치들 큐에 삽입
        if i>0:
            if l[i-1][j]==0:
                q.append((i-1,j))
        if i<n-1:
            if l[i+1][j]==0:
                q.append((i+1,j))
        if j>0:
            if l[i][j-1]==0:
                q.append((i,j-1))
        if j<m-1:
            if l[i][j+1]==0:
                q.append((i,j+1))
            

for i in range(n):
    for j in range(m):
        if l[i][j]==0:
            count+=1
            fill(i,j)

print(count)