# 상하좌우

N = int(input())
commands = [ i for i in input().split()]

location = [1,1]

for command in commands:
    if command=='R' and location[1]<N:
        location[1] += 1
    elif command=='L' and location[1]>1:
        location[1] -= 1
    elif command=='U' and location[0]>1:
        location[0] -= 1
    elif command=='D' and location[0]<N:
        location[0] += 1

print(location)