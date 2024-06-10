N=int(input())
arr=list(map(int,input().split()))

def solution(arr1):
    arr2=[0]*len(arr1)
    arr2[0]=arr1[0]; arr2[1]=arr1[1]
    max_val = max(arr2[0], arr2[1])
    for idx in range(2,len(arr1)):
        arr2[idx] = max(arr2[idx-2]+arr1[idx], arr2[idx-1])
        if arr2[idx]>max_val:
            max_val = arr2[idx]
    return max_val

print(solution(arr))