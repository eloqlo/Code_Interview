def solution(arr):
    x=0 
    while True:
        flag=True
        for i, ele in enumerate(arr):
            if ele>=50 and ele%2==0:
                ele=ele//2
                arr[i]=ele
                flag=False
            elif ele<50 and ele%2==1:
                ele=ele*2+1
                arr[i]=ele
                flag=False
        
        if flag:
            break
        x+=1
        
    return x