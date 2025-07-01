# ! WRONG !

n = int(input())
li = list(map(int,input().split()))

dp1=[1]*n
for i in range(n):
    best=li[i]
    for j in range(i+1,n):
        if best<li[j]:
            best=li[j]
            dp1[i]+=1

dp2=[1]*n
for i in range(n-1,-1,-1):
    best=li[i]
    for j in range(i-1,-1,-1):
        if best<li[j]:
            best=li[j]
            dp2[i]+=1

print(max(max(dp1),max(dp2)))