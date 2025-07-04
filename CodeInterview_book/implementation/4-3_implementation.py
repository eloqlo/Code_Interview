# 게임 개발
"""
Rule
    4면 중, 시계 반대방향으로 가보지 않은 곳을 방문한다.

Map
    1 1 1 1 1 1
    1 0 0 0 0 1
    1 0 1 0 0 1
    1 1 0 0 0 1
    1 1 1 1 1 1
    
Technique
    dx, dy 라는 별도의 리스트를 만들어서 접근하면 쉽다.
    
Feedback
    푸는 과정에서, 알고리즘을 정확히 먼저 정의할 필요가 있겠다.
    방향을 설정해서 푸는 문제는 dx, dy 리스트를 만들어서 이용하는게 편리하대.
"""
import sys

# 다음 방문장소.
def next_visit(x,y, d):
    global world
    global dx
    global dy
    
    for _ in range(4):
        d = (d+1)%4 # 방향 shift
        
        if world[y+dy[d]][x+dx[d]]==1:
            d = (d+1)%4
        elif (x+dx[d],y+dy[d]) in went:
            d = (d+1)%4
        else:
            # 다음 방향이 물도 아니고, 방문한곳도 아니면,
            
            x += dx[d]; y += dy[d]
            went.append((x,y))
            
            return x, y, d
    return 0,0, False

        
N, M = map(int,sys.stdin.readline().strip().split())
x ,y, d = map(int, sys.stdin.readline().strip().split())
world = []
for _ in range(N):
    world.append([i for i in map(int,input().split())])

dx = [0,1,0,-1]
dy = [1,0,-1,0]

went = [(x,y)]


while True:
    x, y, d = next_visit(x, y, d)
    if d==False: break
    
# len(방문한적 리스트) 를 출력해준다.
print(len(went))

##################################################################################

"""
규칙에 맞게 경우의 수 쪼개어 알고리즘을 구현했다.
그 과정에서 global 변수 쓰였음.
-> global 푸는데 쓸 수 만 있으면 무조건 안좋은게 아니구나. 좁은 시야.
"""