n,m = map(int,input().split())

matrix = []

for i in range(n):
    tmp = input()
    line = [i for i in map(int,tmp.split())]
    matrix.append(min(line))
    
print(max(matrix))