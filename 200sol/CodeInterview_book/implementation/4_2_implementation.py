# 시각
"""
전체 데이터 범위가 100,000 이하이다.
그리고 시간 제한도 2초이다.
따라서 하나하나 세서 풀 수 있는 문제이다.

- 실전이었다면, 데이터 범위와 시간 제한을 보고 접근했어야 정답이었다.
- 문제 똑바로 읽자.

- 새로운 표현 GAIN
    ```if 'a' in 'abcdefg': pass```
    이런 식으로 if 문에서 in 이 사용되는구나.
    
"""

import sys

N = int(sys.stdin.readline().strip())
# a = [j for i in map(str,range(60)) for j in i]
# b = [j for i in map(str,range(24)) for j in i]

# # 00-60 중에 몇개인지
# min_sec = a.count('3')*60 + a.count('3')

# # 00-24 중에 몇개인지
# if N<3:
#     print(min_sec*N)
# elif 3<=N<13:
#     print(min_sec*N + 60*60)
# elif 13<=N<23:
#     print(min_sec*N + 60*60*2)
# elif N==23:
#     print(min_sec*N + 60*60*3)


# 3중 for 문
counter = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            tmp = str(i)+str(j)+str(k)
            if tmp.count('3')!=0:
                counter+=1
print(counter)