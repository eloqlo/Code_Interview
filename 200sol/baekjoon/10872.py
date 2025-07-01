n = int(input())
val = 1

def printer(n):
    global val
    if n==0:
        return
    
    val*=n
    if n==1:
        return
    printer(n-1)
printer(n)    
print(val)