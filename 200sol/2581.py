import sys

# m보다 작은 모든 소수를 list에 저장합니다.
decimal_list=[2]
def decimal(m,n):
    global decimal_list
    
    if decimal_list[-1]<n:
        start = decimal_list[-1]+1
        for num in range(start,n+1):
            flag=False
            for decimal_val in decimal_list:
                if num%decimal_val==0:
                    flag=True
                    break
            if flag:
                continue
            else:
                decimal_list.append(num)
    sum_result=0
    min_result=1e+4
    for val in decimal_list:
        if m<=val and n>=val:
            if val<min_result:
                min_result=val
            sum_result+=val
    if sum_result!=0:
        print(sum_result,min_result, sep='\n')
    else:
        print(-1)
    
if __name__=="__main__":
    m=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    decimal(m,n)