def solution(arr, flag):
    X=[]
    for i in range(len(arr)):
        if flag[i]:
            X+=[arr[i]]*(arr[i]*2)
        else:
            for _ in range(arr[i]):
                X.pop(-1)
    return X