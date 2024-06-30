import sys
N,M,H = map(int, sys.stdin.readline().split())
sadari = [[0] * N for _ in range(H)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    sadari[a-1][b-1] = 1

def bebero():
    for i in range(N):
        start_num = i
        for j in range(H):
            if sadari[j][start_num]==1:
                start_num += 1
            elif start_num>0 and sadari[j][start_num-1] == 1:
                start_num -= 1
        if i != start_num:
            return False
    return True

def dfs(cnt, x, y):
    global answer
    if answer <= cnt:
        return
    if bebero():
        answer = min(answer, cnt)
        return
    if cnt == 3:
        return
    for i in range(x, H):
        for j in range(0, N - 1):
            if sadari[i][j] == 0:
                sadari[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                sadari[i][j] = 0
answer = 4
dfs(0,0,0)
if answer>3:
    answer = -1
print(answer)