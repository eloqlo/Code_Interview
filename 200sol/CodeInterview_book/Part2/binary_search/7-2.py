# 이진 탐색
"""부품 탐색"""

n = int(input())
products = list(map(int,input().split()))
products.sort()  # O(NlogN)
m = int(input())
requests = list(map(int,input().split()))

def bs(target, archive, st, ed):
    if st>ed:
        return False
    mid = (st+ed)//2   # check
    if archive[mid]==target:
        return True
    elif archive[mid]<target:
        return bs(target, archive, mid+1, ed)
    elif archive[mid]>target:
        return bs(target, archive, st,mid-1)


for ele in requests:
    if bs(ele, products, 0, len(products)-1):
        print('yes')
    else:
        print('no')