# 공정 데이터 중 감소하는 순서로 정리해야 할 때 필요한 알고리즘 될 수 있겠다.
# 잘 배워놓자! 훗날 언젠가 쓰일, 응용될 알고리즘이야.

"""
https://www.acmicpc.net/problem/11053
< 핵심 >
- 개수만 구한다.
- 걍 이건 일단 외워두자.
"""
N = int(input())
arr = list(map(int, input().split()))

def update(tmp, ele, debug):
    if tmp[-1] < ele:
        tmp.append(ele)
        return tmp

    # Binary Search
    st = 0
    ed = len(tmp)-1
    for _ in range(len(tmp)+1):
        mid = (st + ed) // 2
        if tmp[mid] == ele:
            return tmp
        elif ele < tmp[mid]:
            ed = mid-1
        else:
            st = mid+1

        if st > ed:
            idx = max(st,ed)
            tmp[idx] = ele
            break
    return tmp

def solution(arr,debug=False):
    tmp = []
    for ele in arr:
        # start
        if len(tmp)==0:
            tmp.append(ele)
            continue
        tmp = update(tmp, ele, debug)
    return len(tmp)

print(solution(arr))