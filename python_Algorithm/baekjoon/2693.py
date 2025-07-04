import sys

N = int(input())
out=[]
for _ in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    # count sort
    result=[0]*1000
    
    for ele in li:
        result[ele-1] += 1
    count=0
    for j, ele in enumerate(result):
        if ele!=0:
            count+=1
        if count==8:
            out.append(j+1)
            break

for ele in out:
    print(ele)