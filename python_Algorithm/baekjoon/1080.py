import sys

n,m = map(int,input().split())

a=[]
for _ in range(n):
    a.append([i for i in map(int,sys.stdin.readline().strip())])
b=[]
for _ in range(n):
    b.append([i for i in map(int,sys.stdin.readline().strip())])
    
print(a,b,sep='\n')