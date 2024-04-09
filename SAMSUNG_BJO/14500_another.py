N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]

maxi = max(map(max, arr))
result = 0

def dfs(n, s, lst):
  global result

  # 가지치기: <훌륭하다>
  if result >= s + maxi * (4 - n):
    return

  # 종료 조건
  if n == 4:
    result = max(s, result)
    return

  # 도형의 모든 칸에서 탐색
  for ci, cj in lst:
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      ni, nj = ci + di, cj + dj
      if ni >= 0 and ni < N and nj >= 0 and nj < M and visit[ni][nj] == 0:
        visit[ni][nj] = 1
        dfs(n + 1, s + arr[ni][nj], lst + [(ni, nj)])
        visit[ni][nj] = 0

for i in range(N):
  for j in range(M):
    visit[i][j] = 1
    dfs(1, arr[i][j], [(i, j)])

print(result)