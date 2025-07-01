import sys

a,b = sys.stdin.readline().split()

# 두 문자열이 얼마나 같은지 판별
def same(a:str, b:str):
    count = []
    # 차이만큼 비교해보고, max를 출력
    for j in range(len(b)- len(a)+1):
        count += [0]
        for i in range(len(a)): 
            if a[i] != b[j+i]:
                count[j] += 1
    
    # print(count)
    return min(count)

print(same(a,b))