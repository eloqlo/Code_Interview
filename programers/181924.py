def solution(arr, q):
    for i, j in q:
        t1=arr[i]
        t2=arr[j]
        arr[i]=t1
        arr[j]=t2
    return arr