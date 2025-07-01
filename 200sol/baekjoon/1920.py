"""
https://www.acmicpc.net/blog/view/109

- Binary search - O(logN) 사용해야한다.
- in 연산자: Sequential Search - O(N)

"""

n = int(input())
a = list(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))
a.sort()

def bs(head, tail, val, li):
    """
    return True if search complete
    return False if no value
    """
    while head<=tail:
        mid = (head+tail)//2
        if li[mid]==val:
            return True
        elif li[mid]<val:
            head = mid+1
        elif li[mid]>val:
            tail = mid-1
    return False

    
for val in b:
    # Binary Search here
    head = 0
    tail = n-1
    mid = (head+tail)//2
    
    if bs(head, tail, val, a)==True:
        print(1)
    else:
        print(0)