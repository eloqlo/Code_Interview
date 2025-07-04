def solution(N):
    len_div_N = len(N)//2
    li_N = list(map(int, N))
    sum1, sum2 = sum(li_N[:len_div_N]), sum(li_N[len_div_N:])
    if sum1==sum2:
        print("LUCKY")
    else:
        print("READY")

N = input()
solution(N)