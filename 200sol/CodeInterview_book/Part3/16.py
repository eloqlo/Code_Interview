# https://www.acmicpc.net//problem/14502
# brute force + bfs
"""
< ALGORITHM >
1. consider every circumstances where I put the wall
    - 250,000 * K
2. calculate remain area
    - K= O(bfs) < 100
possible
"""
from collections import deque
import copy

N,M=map(int,input().split())
og_map=[]
for _ in range(N):
    og_map.append(list(map(int,input().split())))

# return area with walls on copy_map
def search(walls, og_map, og_virus):
    copy_map=copy.deepcopy(og_map)
    virus=copy.deepcopy(og_virus)
    mx=[-1,1,0,0]
    my=[0,0,-1,1]
    for loc in walls:
        copy_map[loc[0]][loc[1]]=1
    
    while virus:
        virus_tmp=deque()
        while virus:
            vp=virus.popleft()
            x,y = vp[0],vp[1]
            for i in range(4):
                new_x=x+mx[i]; new_y=y+my[i]
                if (i==0 and x!=0) or (i==1 and x!=N-1) or (i==2 and y!=0) or (i==3 and y!=M-1):
                    if copy_map[new_x][new_y]==0:
                        copy_map[new_x][new_y]=2
                        virus_tmp.append((new_x,new_y))
        virus=virus_tmp
    count=0
    for i in range(N):
        for j in range(M):
            if copy_map[i][j]==0:
                count+=1
    return count, copy_map

virus=deque()
for i in range(N):
    for j in range(M):
        if og_map[i][j]==2:
            virus.append((i,j))

walls=[]
max_area=0
for x1 in range(N):
    for y1 in range(M): 
        if og_map[x1][y1]==0:
            walls.append((x1,y1))
            for x2 in range(x1,N):
                for y2 in range(M):
                    if x2==x1 and y2<=y1:
                        continue
                    if og_map[x2][y2]==0:
                        walls.append((x2,y2))
                        for x3 in range(x2,N):
                            for y3 in range(M):
                                if x3==x2 and y3<=y2:
                                    continue
                                if og_map[x3][y3]==0:
                                    walls.append((x3,y3))
                                    area, copy_map = search(walls, og_map, virus)
                                    if max_area<area:
                                        max_area=area
                                    walls.pop()
                        walls.pop()
            walls.pop()

print(max_area)
