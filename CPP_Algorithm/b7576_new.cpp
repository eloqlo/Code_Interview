#include <deque>
#include <iostream>
using namespace std;

int arr[1001][1001];
bool visited[1001][1001];
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,1,-1};
int n, m, ans = -1;
typedef struct{
    int x;
    int y;
} tmt;
deque<tmt> v;

void bfs(tmt cur)
{
    visited[cur.x][cur.y] = 1;
    for (int i=0; i<4; i++)
    {
        int nx = cur.x + dx[i];
        int ny = cur.y + dy[i];
        if (nx<0 || ny<0 || nx>=m || ny>=n)
            continue;
        if (visited[nx][ny] || arr[nx][ny]!=0)
            continue;
        visited[nx][ny] = 1;
        arr[nx][ny] = arr[cur.x][cur.y] + 1;
        v.push_back({nx,ny});
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for (int i = 0; i < m; i++)
    {
        for (int j=0; j<n; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == 1)
                v.push_back({i,j});
        }
    }

    while (!v.empty())
    {
        tmt start = v.front();
        v.pop_front();
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