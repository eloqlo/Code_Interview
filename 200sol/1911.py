n, l = map(int, input().split())
arr1=[]
for _ in range(n):
    str,end = map(int,input().split())
    arr1.append([str,end])  # 인덱스로 저장.

arr1.sort()
maximum = arr1[-1][1]
count = 0
left = 0
# O(K)
for idx,(s,e) in enumerate(arr1):
    # calc count
    num = e-s
    if idx!=0:
        # 다음순서로 넘어가는 애들 처리부분
        tmptmp = s-last_index<left 
        if tmptmp!=0:
            num-=tmptmp

    tmp = num//l
    if num%l!=0:
        tmp+=1
    count += tmp

    # calc tmp
    left = l-(num%l)
    last_index = e
    tmptmp=0

print(count)