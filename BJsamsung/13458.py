N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())

answer=len(A)
for Ai in A:
    Ai -= B

    if Ai<=0:
        continue
    elif Ai<=C:
        answer+=1
    else:
        answer += Ai//C
        if Ai%C != 0:
            answer += 1

print(answer)