# 나는 직무에 따라 움직인다. 재미가 중요해.
# 필요한 역량들을 설득력있게 준비해야겠다. 겁먹지 말기.
# 사회성 필요하면, 알바로 충족하기.
# 코테는 답이 정해진거지만, 현업의 정해지지 않은 답을 창의적이고 효율적으로 풀어나가고싶다.
# 그리고 그 결과가 가치있는 것 이었으면 좋겠고, 대우를 잘 해줬으면 좋겠다.

import sys

numbs = []
while True:
    numbs.append(sys.stdin.readline().rstrip())
    if numbs[-1]=='0': break
result = []

for numb in numbs:
    # if numb%2==0:
    numb_len = len(numb)//2
    flag = False
    
    for i in range(numb_len):
        if numb[i] != numb[-(i+1)]:
            flag = True
    
    if flag:
        result.append('no')
    else:
        result.append('yes')
result.pop()

for word in result:
    print(word)