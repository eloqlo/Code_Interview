# B의 가장 작은 것과 A의 가장 큰 수가 곱해지면?

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

# sort A in upward
a.sort(reverse=True)
# sort B in downward
b.sort()

ans=0
for idx in range(n):
    ans += a[idx] * b[idx]

print(ans)