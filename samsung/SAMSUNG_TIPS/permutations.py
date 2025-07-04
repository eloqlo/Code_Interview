arr = [1,2,3]
visited = [0] * len(arr)

# 순서 상관 Y / 중복 N
def permutations(n, new_arr):
    global arr, visited
    if len(new_arr) == n:
        print(new_arr)
        return

    for i in range(len(arr)):
        if visited[i]==0:
            visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            visited[i] = 0


permutations(2, [])