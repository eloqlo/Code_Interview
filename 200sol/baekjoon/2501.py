# 약수 구하기

n,k = map(int, input().split())

# 약수 구하기
yaksu = []
for num in range(1,n+1):
    if n%num==0:
        yaksu.append(num)

# K번째 수 추출
if k<=len(yaksu):
    print(yaksu[k-1])
else:
    print(0)