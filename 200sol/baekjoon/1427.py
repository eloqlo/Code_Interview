li = [x for x in map(int,input())]

li.sort(reverse=True)

strr=''

for i in li:
    strr+=str(i)

print(strr)