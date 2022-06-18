import sys

n,m = map(int, sys.stdin.readline().strip().split())

# 2차원 리스트 생성
g = []
for i in range(n):
    g.append(list(map(int,input())))

# main에서 모든 칸을 이거로 조회할거임. 그거 생각
# stack 구조가 맞지. 먼저 방문한애 위로 쌓이니깐
def dfs(x,y):
    # 영역 벗어났으면 False(바로 나옴)
    if x<0 or y<0 or x>n-1 or y>m-1:
        return False
    # 만일 미개척지면?
    if g[x][y] == 0:
        g[x][y] = 1   # 개척하고
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)  # 주위 다 채우기!
        return True # 주변 한뭉탱이들 채우고 True 반환.
    return False # 이미 개척된놈이면 False 반환(count x)

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            count += 1

print(count)