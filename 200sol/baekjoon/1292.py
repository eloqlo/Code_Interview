a,b = map(int,input().split())

li=[]
i=1
while(True):
    li.extend([i]*i)
    i+=1
    if len(li)>1000:
        break

print(sum(li[a-1:b]))