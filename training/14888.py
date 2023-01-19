# 수들의 합 -- silver 5
"""
1.  수학적으로 hard coding 할 방법은 보이지 않는다.

    - 기존 유형일까?
    {그리디, 구현, dfs, bfs, 정렬, 탐색, DP, 최단경로, 그래프}

2.  완전탐색이다. 정해진 연산자 배열중 가장 적합한 경우를 찾아야 하는거로 볼 수 있네.
    실전이었다면 시간상 완전탐색으로 시도해봤겠지만, 2분만 더 깊게 생각해본다.
    
3.  랜덤성이 너무 크다. 연산자들에 따라서 바뀌는것이 너무 많고, 이건 구현이 아닌 탐색으로 접근해야한다.

"완전탐색"
""""""
천천히 하나하나 제대로 이해하자.
한번에 풀려하면 안풀리네 천천히 짚고 넘어가면서 봐야하는 부분이군.
처음부터 어떻게 잘해, 쎈수학b스텝도 몇번 풀어봐야 아는거지.
"""

import sys

n = int(sys.stdin.readline())
ele1 = list(map(int, sys.stdin.readline().split()))
ele2 = list(map(int, sys.stdin.readline().split()))
max_val = 1e+9
min_val = -1e-9


# dfs를 쓸 경우엔, node엔 어떤게 오고, 어떤 traversal을 거칠 것인지 알아야겠구나
def dfs(i, result):
    """
    i       과정 도달 확인용
    result  각 step 별 계산 output
    """
    global ele2, max_val, min_val

    if i==n:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
    else:
        # 더하기
        if ele2[0] > 0:
            ele2[0] -= 1
            dfs(i+1, result + ele1[i])
            ele2[0] += 1
        # 뺄셈
        if ele2[1] > 0:
            ele2[1] -= 1
            dfs(i+1, result - ele1[i])
            ele2[1] += 1
        # 곱하기
        if ele2[2] > 0:
            ele2[2] -= 1
            dfs(i+1, result * ele1[i])
            ele2[2] += 1
        # 나누기
        if ele2[3] > 0:
            ele2[3] -= 1
            dfs(i+1, result / ele1[i])
            ele2[3] += 1
    
max_val, min_val = dfs(1, ele1[0])

print(max_val, min_val, sep='\n')

"""
내가 몰랐던건 이거였고, 내가 알게된건 이거다.

1. 함수를 만들 때, 뭐를 넣고 뭐가 나와야할지를 정해야하겠구나.
2. recursive 를 통해서 dfs를 하려면, 함수가 step별로 나눠서 판단하므로, 내 문제를 step별로 나눠서 봐야겠다?
3. 그리고, 적절한 통제변수들을 전달하면서 과정의 논리를 관리해야겠구나.
"""