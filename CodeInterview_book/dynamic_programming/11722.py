N = int(input())
arr = list(map(int,input().split()))

def solution(arr):
    tmp = [arr[0]]
    for ele in arr[1:]:
        tmp = update_tmp(tmp, ele)
    return len(tmp)

def update_tmp(tmp,ele):
    if ele < tmp[-1]:
        tmp.append(ele)

    st=0
    ed=len(tmp)-1
    for _ in range(len(tmp)+1):
        mid = (st+ed)//2
        if tmp[mid] < ele:
            ed = mid-1
        elif tmp[mid] > ele:
            st = mid+1
        elif tmp[mid] == ele:
            return tmp
        else:
            raise Exception("ERROR")

        if st > ed:
            tmp[max(st,ed)] = ele
            break

    return tmp


print(solution(arr))