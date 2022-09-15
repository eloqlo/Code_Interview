"""
시간초과...

implementation은 쉬운데, 
복잡도에서 고려해야할것이 있네

"""
import sys
n,m = map(int, sys.stdin.readline().strip().split())


# O(N)
d = []
for _ in range(n):
    d.append(sys.stdin.readline().strip())
# b=[]
# for _ in range(m):
#     b.append(sys.stdin.readline().strip())

# # O(N^2)
dbj = []
# for name in d:
#     if name in b:
#         dbj.append(name)

for _ in range(m):
    name = sys.stdin.readline().strip()
    if name in d:
        dbj.append(name)

# O(NlogN)
dbj.sort()
print(len(dbj))
for name in dbj:
    print(name)