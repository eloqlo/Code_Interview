n = int(input())

m = 2*n-1

for i in range(1,n+1):  # 1,2, ... , n
    # for l in range(n-i):
    #     print(' ', end='')
    # for l in range(2*i-1):
    #     print('*', end='')
    print(" "*(n-i) + "*"*(2*i-1))

    