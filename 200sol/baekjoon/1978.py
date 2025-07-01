# 소수 찾기

N = int(input())
arr = list(map(int,input().split()))

sosu_list=[2]

# n이 소수인지 판단
def is_sosu(n):
    global sosu_list
    if n<2:
        return False
    
    #1 n에 맞추어 소수 리스트 업데이트
    max_sosu = sosu_list[-1]
    if n>max_sosu:
        # O(N^2)
        for val in range(max_sosu+1, n+1):
            flag=False
            for sosu in sosu_list:
                # 기존 소수로 나눠지면 일반수다.
                if val%sosu==0:
                    flag=True
                    break
            if flag:
                continue
            else:
                # 가진 소수로 나눠지지 않는 기존 소수 이상의 수면, 소수이다.
                sosu_list.append(val)
                print(sosu_list[-1])
    
    #2 n이 소수리스트에 있는지 확인
    if n in sosu_list:
        return True
    else:
        return False

count=0
for n in arr:
    if is_sosu(n):
       count+=1
print(count)