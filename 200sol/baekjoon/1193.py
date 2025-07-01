x = int(input())
tmp = 1
i=1

# O(N-K)
while(True):
    if tmp>x:
        i -= 1
        val = tmp-i
        break
    
    tmp += i
    i+=1

print

# O(N-K)
j=1
while(val!=x):
    val+=1
    j+=1

if i%2==0:
    print(j,i-j+1,sep='/')
else:
    print(i-j+1,j,sep='/')