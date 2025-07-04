N = int(input())
arr = list(map(int, input().split()))
def solution(arr):
    tmp=[]
    for ele in arr:
        if len(tmp)==0:
            tmp.append(ele)
            continue
        tmp = get_arr(tmp, ele)
    return len(arr)-len(tmp)

def get_arr(tmp, ele):
    if tmp[-1] > ele:
        tmp.append(ele)
        return tmp

    # Binary Search
    st = 0
    ed = len(tmp)-1
    for _ in range(len(tmp)+1):
        mid = (st+ed)//2
        if tmp[mid] == ele:
            return tmp
        elif ele < tmp[mid]:
            st = mid+1
        else:
            ed = mid-1

        if st>ed:
            idx = max(st,ed)
            tmp[idx] = ele
            break
    return tmp

print(solution(arr))