# 존나어렵, 흙길 채우기
n, l = map(int, input().split())
arr1=[]
for _ in range(n):
    str,end = map(int,input().split())
    arr1.append([str,end])  # 인덱스로 저장.

arr1.sort()
maximum = arr1[-1][1]
count = 0

# 너무 복잡하게 짠다. 다시 생각해보기.


print(count)