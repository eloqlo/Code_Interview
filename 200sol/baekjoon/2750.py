n=int(input())
li=[]
for _ in range(n):
    li.append(int(input()))

# selection sort
# O(N^2)
for i in range(n):
    for j in range(i+1,n):
        if li[j]<li[i]:
            tmp=li[i]
            li[i] = li[j]
            li[j] = tmp
print(li)

# insertion sort
# 이미 정렬이 많이 되어있는 경우, 엄청 빠른..!
# O(N^2)
for i in range(1,n):
    for j in range(i):
        if li[i]<=li[j]:
            tmp=li.pop(i)
            li.insert(j,tmp)
        if j+1==i:
            tmp=li.pop(i)
            li.insert(j+1,tmp)
print(li)


# quick sort
# complicated...
def quick_sort(array, start, end):
    pass