import sys

input = int(sys.stdin.readline().strip())

count = 0
def calc(i):
    global count
    print('count: ',count,', i: ',i)
    if i==1:
        print('return: ', count)
        return count
    elif i%2==0:
        count += 1
        calc(i//2)
    elif i%3==0:
        count += 1
        calc(i//3)
    else:
        count += 1
        calc(i-1)


result = calc(input)
print(result)