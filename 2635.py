n = int(input())
result=[]

"""
일일히 돌면서 count 하는 알고리즘.
"""

if n>2:
    max_num=0
    for num in range(1,n):
        buffer=[n]  
        buffer.append(num)
        for i in range(n):
            try:
                temp = buffer[i]-buffer[i+1]
            except:
                break
            if temp >= 0:
                buffer.append(temp)
            elif len(buffer)>max_num:
                max_num=len(buffer)
                result=buffer
    print(len(result))
    for i in result:
        print(i,end=' ')
elif n==1:
    print(3)
    print(1,1,0)
elif n==2:
    print(4)
    print(2,1,1,0)