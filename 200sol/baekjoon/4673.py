# self number

"""
어떤 숫자 n의 self-number을 구하는 함수
"""
def d(n):
    tmp = list(map(int, str(n)))
    return n + sum(tmp)

li = [0]*1000000

for i in range(1,10001):
    li[d(i)-1]+=1
    
for i in range(10000):
    if li[i]==0:
        print(i+1)