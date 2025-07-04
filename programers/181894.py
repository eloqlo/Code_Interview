def solution(arr):
    flag=False
    start=-1
    for i,ele in enumerate(arr):
        if ele==2 and flag==False:
            flag=True
            start=i
        if ele==2:
            end=i
    if start==-1:
        return [-1]
    return arr[start:end+1]