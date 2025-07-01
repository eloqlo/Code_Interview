# 피보나치 수

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    
    tail=0
    head=1
    # calc fib num
    for _ in range(n-1):
        tmp = head
        head += tail
        tail = tmp
    return head

print( fib(int(input())) )