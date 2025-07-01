# Dynamic Programming
# 1로 만들기

def computations(x):
    results=set()
    if x%5==0:
        results.add(x//5)
    if x%3==0:
        results.add(x//3)
    if x%2==0:
        results.add(x//2)
    results.add(x-1)
    return results

x = int(input())
count=0
dpTable={x}  # 이미 계산한 녀석들
toCompute={x}  # 이번 count에서 계산할 녀석들
flag=False
for _ in range(300000):
    count += 1
    for ele in list(toCompute):
        results = computations(ele)
        if 1 in results:
            flag = True
            break
        toCompute = toCompute|results   # 계산 예정 stack 추가
        dpTable = dpTable|results   # 이번 계산 결과 DPtable에 추가
    toCompute-=dpTable  # 안본 애들만 계산 다시 해준다.
    if flag:
        break

print(count)


"""
책에선, N별로 1에 도달하는 가장 짧은 hops를 구하는 방식으로 O(N)로 풀음.
"""