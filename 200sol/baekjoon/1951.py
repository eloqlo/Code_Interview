N = input()

answer=0
for i in range(1,len(N)):
    answer += 9*i*10**(i-1)
answer += len(N)*(int(N) - 10**(len(N)-1) + 1)

print(answer%1234567)