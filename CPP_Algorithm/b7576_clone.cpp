#include <bits/stdc++.h>
using namespace std;

int arr[1001][1001];
bool visited[1001][1001];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int n, m, ans = -1;
queue<pair<int, int>> v;

// 하루치만 익은 토마토를 저장
void bfs(pair<int, int> cur)
{
    visited[cur.first][cur.second] = true;
    for (int i = 0; i < 4; i++)
    {
        int nextX = cur.first + dx[i];
        int nextY = cur.second + dy[i];
        if (nextX < 0 || nextY < 0 || nextX >= m || nextY >= n)
            continue;
        if (visited[nextX][nextY] || arr[nextX][nextY] != 0)
            continue;
        visited[nextX][nextY] = true;
        arr[nextX][nextY] = arr[cur.first][cur.second] + 1;
        v.push({nextX, nextY});
    }
}
int main()
{
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m;

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> arr[i][j];
            // 익은 토마토 위치 우선 저장
            if (arr[i][j] == 1)
                v.push({i, j});
        }
    }

    // 익은 토마토 전파시키기
    while (!v.empty())
    {
        pair<int, int> start = v.front();
        v.pop();
        bfs(start);
    }

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (arr[i][j] == 0)
            {
                cout << -1;
                return 0;
            }
            else
                ans = max(ans, arr[i][j]);
        }
    }
    cout << ans - 1;
}