# 음료수 얼려먹기

"""
1. 한칸씩 다 방문할거다
2. 특정 칸 방문 시, 인접한 0칸들 다 체크할거다.
3. 그렇게 모든 칸 돌면서 count 하면 되겠다.

공간이 연결돼있다고 표현할 수 있으므로, 그래프 형태로 모델링 할 수 있다.
"""

# inputs
n, m = map(int,input().split())
tray = []
for _ in range(n):
    tray.append([i for i in map(int,input())])

# 0이면, 인접 0칸들 싹 방문 후, True 반환한다.
def travel(i,j):
    if tray[i][j]==1: 
        return False

    tray[i][j] = 1
    if i>0:
        travel(i-1,j)
    if i<n-1:
        travel(i+1,j)
    if j>0:
        travel(i,j-1)
    if j<m-1:
        travel(i, j+1)
    
    return True


count = 0
for i in range(n):
    for j in range(m):
        if travel(i,j): 
            count+=1

print(count)