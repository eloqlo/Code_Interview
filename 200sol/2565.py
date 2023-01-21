# # input - 순서쌍
# n = int(input())
# li=[]
# for _ in range(n):
#     a_sample, b_sample = map(int, input().split())
#     li.append((a_sample,b_sample))

# # index별 꼬인개수 파악 function
# def how_many(li):
#     a_i2n = []
#     # O(N^2 < 10000)
#     for a_a,a_b in li:
#         count=0
#         for b_a,b_b in li:
#             if a_a==b_a:
#                 continue
#             if a_a>b_a and a_b<b_b:
#                 count+=1
#             if a_a<b_a and a_b>b_b:
#                 count+=1
#         a_i2n.append(count) # 해당 a랑 겹친 개수를 list에 저장
#     return a_i2n

# count = 0
# a_i2n = how_many(li) # 시작시점 꼬인 list
# while(sum(a_i2n)!=0):
#     worst_i = a_i2n.index(max(a_i2n))
#     # li에서 제일 꼬인거 제거
#     li.pop(worst_i)
#     a_i2n = how_many(li)
#     count+=1    # counting
    
# print(count)

n = int(input())
a = sorted([list(map(int, input().split())) for _ in range(n)])

dp=[]
for i in range(n):
    count=0
    for j in range(i+1,n):
        if a[i][1]<a[j][1]:
            count+=1
    dp.append(count)

a.sort(reverse=True)
for i in range(n):
    count=0
    for j in range(i+1,n):
        if a[i][1]<a[j][1]:
            count+=1
    dp.append(count)



print(n-max(dp))