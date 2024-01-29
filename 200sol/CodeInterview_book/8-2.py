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
dpTable={x}
toCompute={x}
for _ in range(300000):
    count+=1
    for ele in toCompute:
        results=computations(ele)
        if 1 in results:
            break
        toCompute=results - dpTable
        dpTable=dpTable.union(results)
        

print(count)