#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

typedef struct{
    int r;
    int c;
}arr_loc;

int N;
int dr[4] = {-1,1,0,0};
int dc[4] = {0,0,1,-1};
vector<vector<int>> arr;
vector<vector<bool>> visit;

void bfs(int i, int j, int water);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i=0; i<N; i++){
        vector<int> arr_line;
        int tmp;
        for (int j=0; j<N; j++){
            cin >> tmp;
            arr_line.push_back((int)tmp);
        }
        arr.push_back(arr_line);
    }
    for (int i=0; i<N; i++){
        vector<bool> visit_line;
        for (int j=0; j<N; j++){
            visit_line.push_back(false);
        }
        visit.push_back(visit_line);
    }

    int max_safe_place_count = 0;
    for (int water=0; water<100; water++){
        int cur_safe_place_count = 0;

        /* Clear visit */
        for (int i=0; i<N; i++){
            for (int j=0; j<N; j++){
                visit[i][j] = false;
            }
        }
    
        
        /* BFS arr */
        for (int i=0; i<N; i++){
            for (int j=0; j<N; j++){
                if (visit[i][j] == false && arr[i][j] > water) {
                    bfs(i, j, water);   // water 이상 땅 visit 처리
                    cur_safe_place_count++;
                }
            }
        }
        if (cur_safe_place_count > max_safe_place_count) {
            max_safe_place_count = cur_safe_place_count;
        }
    }

    cout << max_safe_place_count;
    return 0;
}

/* i,j에 인접한 water초과 영역을 visit처리 */
void bfs(int i, int j, int water){
    visit[i][j] = true;
    deque<arr_loc> dq;
    dq.push_back({i, j});
    while(!dq.empty()){
        arr_loc loc = dq.front();
        dq.pop_front();
        for (int di=0; di<4; di++){
            int nr = loc.r + dr[di];
            int nc = loc.c + dc[di];
            if (nr<0 || nc<0 || nr>=N || nc>=N) continue;
            if (arr[nr][nc] <= water || visit[nr][nc] == true) continue;
            
            visit[nr][nc] = true;
            dq.push_back({nr,nc});
        }
    }
}