# 수열 정렬

n = int(input())
a = [i for i in map(int,input().split())]
p = [0]*n
b = sorted(a)
tmp = [0]*1001

for i in range(n):
    # a_i가 b에서 어디있는지 -> index
    idx = b.index(a[i])
    # p_i는 tmp[a_i] + index
    p[i] = tmp[a[i]]+idx
    # tmp[a_i]+=1
    tmp[a[i]]+=1

for pp in p:
    print(pp, end=' ')