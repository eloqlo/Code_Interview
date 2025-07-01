# 경계선까지 가는데 걸리는 최소의 거리

x,y,w,h = map(int,input().split())

a_x = min(x,w-x)
a_y = min(y,h-y)

print(min(a_x,a_y))