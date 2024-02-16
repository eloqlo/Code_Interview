# https://www.acmicpc.net/problem/18405
from collections import deque

# Input
N,K=map(int,input().split())
cur_virus_pos=deque()
virus_map=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    for j,ele in enumerate(tmp):
        if ele>0:
            cur_virus_pos.append((i,j,ele))
    virus_map.append(tmp)
S,X,Y = map(int,input().split())

# Spread Virus
mx=[-1,1,0,0]
my=[0,0,-1,1]
for _ in range(S):
    tmp_dict = {}
    while cur_virus_pos:
        check=[[False]*N]*N
        virus = cur_virus_pos.popleft()
        for i in range(4):
            new_x=virus[0]+mx[i]
            new_y=virus[1]+my[i]
            if (i==0 and virus[0]!=0) or (i==1 and virus[0]!=N-1) or (i==2 and virus[1]!=0) or (i==3 and virus[1]!=N-1):
                if virus_map[new_x][new_y]==0:
                    virus_map[new_x][new_y]=virus[2]
                    check[new_x][new_y]=True
                    tmp_dict[(new_x,new_y)]=virus[2]
                elif check[new_x][new_y]==True and virus_map[new_x][new_y]>virus[2]:
                    virus_map[new_x][new_y]=virus[2]
                    tmp_dict[(new_x,new_y)]=virus[2]
        
    if len(tmp_dict)==0:
        break
    tmp_keys=tmp_dict.keys()
    tmp_values=tmp_dict.values()
    for k,v in zip(tmp_keys,tmp_values):
        cur_virus_pos.append((k[0],k[1],v))

print(virus_map[X-1][Y-1])