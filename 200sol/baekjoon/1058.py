# Graph
"""
정답 matrix (NxN)를 만들고, 특정 인물과 직접친구 or 건너친구 이면, True를 해당 node에 저장하고, 추후 sum 해줄 예정

그저 적절히 조회했다고 생각한다. 이게 dfs 알고리즘을 사용한건가? 특정 node안에 들어가서 전부 보고 나온거니깐 말이야. 알고리즘은 정형된게 아니라, 상황에 맞게 사용하는거니 dfs 를 써서 풀었다고 말할 수 있나?
깊이로 들어감에 있어서 조건을 만족시켜야하는 경우에 사용되는 DFS
"""
import sys

n = int(input())

# naive matrix 생성
li=[]
result=[]
for _ in range(n):
    li.append([i for i in sys.stdin.readline().strip()])
    result.append([False for _ in range(n)])

# N<50 이라서 복잡도 신경 쓰지 않고 짰다.
# O(N^2logN) 쯤 될듯해.
best = 0
for i in range(n):
    for j in range(n):
        if i==j: continue
        if li[i][j]=='Y':
            result[i][j]=True
            for k, element in enumerate(li[j]):
                if element=='Y' and k!=i:
                    result[i][k]=True   # 2다리 건너는 사이면, 친구!
    if sum(result[i])>best:
        best = sum(result[i])

print(best)
