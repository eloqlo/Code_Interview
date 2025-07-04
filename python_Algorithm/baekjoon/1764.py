N,M = map(int, input().split())

# n1=set()
# ans=[]
# for _ in range(N):
#     n1.add(input())
# for _ in range(M):
#     name = input()
#     if name in n1:
#         ans.append(name)
# ans.sort()
from collections import defaultdict
n1=defaultdict(int)

ans=[]
for _ in range(N):
    n1[input()] += 1
for _ in range(M):
    n=input()
    n1[n] += 1
    if n1[n]==2:
        ans.append(n)
ans.sort()
print(len(ans))
for l in ans:
    print(l)


# """
# 시간초과...
#
# implementation은 쉬운데,
# 복잡도에서 고려해야할것이 있네
#
# """
# import sys
# n,m = map(int, sys.stdin.readline().strip().split())
#
#
# # O(N)
# d = []
# for _ in range(n):
#     d.append(sys.stdin.readline().strip())
# # b=[]
# # for _ in range(m):
# #     b.append(sys.stdin.readline().strip())
#
# # # O(N^2)
# dbj = []
# # for name in d:
# #     if name in b:
# #         dbj.append(name)
#
# for _ in range(m):
#     name = sys.stdin.readline().strip()
#     if name in d:
#         dbj.append(name)
#
# # O(NlogN)
# dbj.sort()
# print(len(dbj))
# for name in dbj:
#     print(name)