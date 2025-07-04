# Dynamic Programming : 한번푼거는 한번만 푼다.
import sys

f = [0,1]

# n번째 피보나치 수열값, f이상 조회시 그 이전꺼 싹다 저장
def fb(n):
    global f
    if len(f)<=n:
        for i in range(len(f),n+1):
            f.append(f[i-1] + f[i-2])
        return f[n-1]
    else:
        return f[n-1]

# n에 필요한 0,1 개수를 반환한다.
def count(n):
    if n==0:
        return 1,0
    elif n==1:
        return 0,1
    else:
        return fb(n), fb(n+1)

# 입력 받아와 처리
n = int(sys.stdin.readline().strip())
for i in range(n):
    input = int(sys.stdin.readline().strip())
    c0,c1 = count(input)
    print(c0,c1)