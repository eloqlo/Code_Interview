import sys

n, k = map(int, sys.stdin.readline().split())

people = [i for i in range(1,n+1)]

index = 0
answer = []
for i in range(n):
    index = ((index+k)-1)%len(people)
    answer.append(people.pop(index))

print('<', end='')
for i in range(n):
    if i!=n-1:
        print(str(answer[i])+', ', end='')
    else:
        print(str(answer[i])+'>')