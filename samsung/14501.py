N = int(input())
arr = []

# 불가능한 상담은 None으로 대체
for i in range(N):
    arr.append(tuple(map(int,input().split())))

max_value = 0
def solution(now, money):
    global arr, max_value
    is_end = now
    for new_now in range(now, N):
        if new_now + arr[new_now][0] <= N:
            money += arr[new_now][1]
            now += arr[new_now][0] + (new_now-now)
            solution(now, money)
            money -= arr[new_now][1]
            now -= arr[new_now][0] + (new_now-now)
        else:
            is_end += 1

    if is_end==N:
        if money > max_value:
            max_value=money
        return

solution(0,0)
print(max_value)