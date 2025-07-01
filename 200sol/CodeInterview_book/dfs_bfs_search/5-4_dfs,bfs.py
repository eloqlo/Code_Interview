# 미로탈출
"""
queue 를 사용해서 bfs로 최단거리 문제 쉽게 해결할 수 있었음.
popleft() 에서 논리오류 났었다.
"""
from collections import deque
import time
import numpy as np

n, m = map(int,input().split())

maze = []
for _ in range(n):
    maze.append([i for i in map(int,input())])

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    count = 0
    
    while True:
        # queue pop
        loc = queue.popleft()
        count += 1
        step = maze[loc[0]][loc[1]]
        
        print(np.array(maze))
        print('loc: ', loc)
        time.sleep(0.5)
        
        if count==1:
            maze[loc[0]][loc[1]] = 0
            
        # 목적지 도착 시 종료
        if loc==(n-1, m-1): 
            break
        
        # 현재 위치 4면 중 갈 수 있는 곳을 queue에 담는다.
        if loc[0]>0:
            new_loc = (loc[0]+dx[0], loc[1]+dy[0])
            if maze[new_loc[0]][new_loc[1]]==1: 
                maze[new_loc[0]][new_loc[1]] += step
                queue.append(new_loc)
        if loc[0]<n-1:
            new_loc = (loc[0]+dx[1], loc[1]+dy[1])
            if maze[new_loc[0]][new_loc[1]]==1:
                maze[new_loc[0]][new_loc[1]] += step
                queue.append(new_loc)
        if loc[1]>0:
            new_loc = (loc[0]+dx[2], loc[1]+dy[2])
            if maze[new_loc[0]][new_loc[1]]==1:
                maze[new_loc[0]][new_loc[1]] += step
                queue.append(new_loc)
        if loc[1]<m-1:
            new_loc = (loc[0]+dx[3], loc[1]+dy[3])
            if maze[new_loc[0]][new_loc[1]]==1:
                maze[new_loc[0]][new_loc[1]] += step
                queue.append(new_loc)
        

    return maze[loc[0]][loc[1]]

print(bfs(0,0))