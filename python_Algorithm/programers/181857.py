def solution(arr):
    ele=2**0
    i=0
    while len(arr)-ele>0:
        i+=1
        ele=2**i
    arr += [0]*(ele-len(arr))
    
    return arr