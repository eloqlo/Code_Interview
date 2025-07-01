def solution(N, arr):

    arr.sort()
    counter = 0
    u = []
    for ele in arr:
        if ele==1:
            counter+=1
            continue
        if len(u)==0:
            u.append(ele)
            continue
        else:
            if len(u)+1 == ele:
                counter += 1
                u = []

    return counter



N = int(input())
arr = list(map(int, input().split()))
print(solution(N,arr))