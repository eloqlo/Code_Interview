from collections import deque

n,m=(3,3)
l=[[1,0,1],
   [1,1,1],
   [0,0,1]]
check=[[False]*m for _ in range(n)]

q=deque()
qq=deque()
q.append((0,0))
count=1; i=0; j=0
while q:
    for _ in range(len(q)):
        i,j=q.popleft()
        if i==n-1 and j==m-1:
            l[i][j]=count
            break
        check[i][j]=True
        l[i][j]=count
        
        if i>0:
            if l[i-1][j]==1 and check[i-1][j]==False:
                qq.append((i-1,j))
        if i<n-1:
            if l[i+1][j]==1 and check[i+1][j]==False:
                qq.append((i+1,j))
        if j>0:
            if l[i][j-1]==1 and check[i][j-1]==False:
                qq.append((i,j-1))
        if j<m-1:
            if l[i][j+1]==1 and check[i][j+1]==False:
                qq.append((i,j+1))
    
    q=qq.copy()
    qq=deque()
    count+=1

print(l[n-1][m-1])