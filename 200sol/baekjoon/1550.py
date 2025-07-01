"""
**알고리즘**

16진수를 자리별로 10진수로 변환한다.
변환한 10진수에 16을 곱해 더해준다.
"""

from collections import deque

num = input()

def maker(num):
    out = 0
    if num=='A':
        out=10
    elif num=='B':
        out=11
    elif num=='C':
        out=12
    elif num=='D':
        out=13
    elif num=='E':
        out=14
    elif num=='F':
        out=15
    else:
        out = int(num)

    return out


tmp = [i for i in map(maker, num)]
tmp = deque(tmp)

# print(tmp)

result = 0
for i in range(len(num)):
    result += tmp.pop()*(16**i)
    # print(result)    

print(result)