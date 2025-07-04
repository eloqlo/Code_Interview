n = int(input())
num_arr = list(map(int,input().split()))
operators = list(map(int,input().split()))


minval=1e+9
maxval=-1e+9
# i=1
def finder(val, i):
    global num_arr, minval, maxval,operators
    
    # 종료 조건
    if i==n:
        if val>maxval:
            maxval = val
        if val<minval:
            minval = val
        return
    
    # 완전탐색
    if operators[0]!=0:
        operators[0]-=1
        finder(val+num_arr[i], i+1)
        operators[0]+=1
    
    # subtraction
    if operators[1]!=0:
        operators[1]-=1
        finder(val-num_arr[i], i+1)
        operators[1]+=1
    
    # multiplication
    if operators[2]!=0:
        operators[2]-=1
        finder(val*num_arr[i], i+1)
        operators[2]+=1
    
    # division
    if operators[3]!=0:
        operators[3]-=1
        if val<0:
            tmp = -val
            tmp = tmp//num_arr[i]
            tmp = -tmp
        else:
            tmp = val//num_arr[i]
        finder(tmp, i+1)
        operators[3]+=1

finder(num_arr[0], i=1)
print(maxval, minval)