""" 개발자는 자신의 한계에 가까운, 
    그리고 더 어렵지만, 
    더 많은 것을 배울 수 있는 
    업무와 프로젝트를 선택해야 한다"""
# 최대 최소

N = int(input())
li = list(map(int,input().split()))

# print(min(li), max(li), sep=' ')


def minmax(li):
    min_ = int(1e+6)
    max_ = int(-1e+6)
    for ele in li:
        if ele>max_:
            max_ = ele
        if ele<min_:
            min_ = ele

    print(min_, max_, sep=' ')

minmax(li)