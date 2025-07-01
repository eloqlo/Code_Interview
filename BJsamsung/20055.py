from collections import deque
n,k = map(int,input().split())
arr = deque( list(map(int,input().split())) )
robot = deque([False]*n)
step = 0
zc=0

while 1:
    step+=1
    #1
    arr.rotate(1)
    robot.rotate(1)
    robot[-1] = False
    #2
    for idx in range(n-2, -1, -1):
        if robot[idx] and (not robot[idx+1]) and arr[idx+1]>0:
            arr[idx+1] -= 1
            robot[idx] = False
            robot[idx+1] = True
            if arr[idx+1] == 0:
                zc += 1
    robot[-1] = False
    #3
    if arr[0] > 0:
        robot[0] = True
        arr[0]-=1
        if arr[0]==0:
            zc+=1
    #4
    if zc>=k:
        break
print(step)