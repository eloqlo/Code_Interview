def solution(array):
    # O(N)
    minval=1000
    flag=False
    for i in range(len(array)):
        
        if array[i]<minval:
            minval=array[i]
            flag = False
        elif array[i]==minval:
            flag = True
    if flag:
        return -1
    else:
        return minval
    

li = [1]

print(solution(li))