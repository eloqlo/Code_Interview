def solution(arr):
    answer = 0
    flag=True
    for i in range(len(arr)):
        for j in range(i):
            if arr[i][j]!=arr[j][i]:
                flag=False
                break
        if not flag:
            break
    return int(flag)

# symmetric 이용한 풀이
def solution(arr):
    return int(arr == list(map(list, zip(*arr))))