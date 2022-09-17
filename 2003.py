"""
n 10000
m 300,000,000

원하는 역량: ?
해결목표: 연속으로 더해서 m이 되는 경우의 수를 체크한다.
예상복잡도: linear하게 돌면서, 그안에서 부분 linear 하게 돈다. O(N^2)
예상시간: N<=10000 이므로, 100,000,000 연산횟수

알고리즘1: 시간초과!
i=0부터 n-1까지 i+1, i+2 원소들 더해가면서 over되는지 체크할거다.

loop i=0부터 i=n-1까지
    if 같으면 
        count+=1
    if 오버되면
        continue
    if max_idx까지 가면
        continue

알고리즘2:
특정놈이 연속더하기 성공을 했으면, 다음 index에서 이전거를 사용하는거다.

"""
import sys

n,m = map(int,sys.stdin.readline().strip().split())

li = list(map(int,sys.stdin.readline().strip().split()))

count = 0

# i부터 li원소를 쭉 더한다.
def my_loop(i):
    val = 0
    for j in range(i,n):
        try:
            val += li[j]
        except:
            break
        if val==m:
            return True
        elif val>m:
            break
    return False
            
for i in range(0,n,10):
    if my_loop(i):
        count+=1
    if my_loop(i+1):
        count+=1
    if my_loop(i+2):
        count+=1
    if my_loop(i+3):
        count+=1
    if my_loop(i+4):
        count+=1
    if my_loop(i+5):
        count+=1
    if my_loop(i+6):
        count+=1
    if my_loop(i+7):
        count+=1
    if my_loop(i+8):
        count+=1
    if my_loop(i+9):
        count+=1
    

print(count)
            

