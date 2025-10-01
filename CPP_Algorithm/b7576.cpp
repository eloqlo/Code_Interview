#include <vector>
#include <deque>
#include <iostream>
#include <string>

using namespace std;

typedef struct{
    int r;
    int c;
}tmt_loc;
typedef struct{
    int val;
    int visit;
} tmt;

deque<tmt_loc> dq;
vector<vector<tmt>> arr;
int unripe = 0;
int dr[4] = {1,-1,0,0};
int dc[4] = {0,0,1,-1};
int bfs(void);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    /* INPUT */
    int M, N;
    cin >> M >> N;
    int tmt_val;
    for (int r=0; r<N; r++){
        vector<tmt> line;
        for (int c=0; c<M; c++){
            cin >> tmt_val;
            line.push_back({tmt_val, 0});
            if (tmt_val==1){
                line[c].visit = 1;      // 시작 토마토 visit 처리
                dq.push_back({r,c});
            }
            else if (tmt_val == 0)
            {
                unripe++;
            }
            
        }
        arr.push_back(line);
    }
    
    /* Algorithm */
    int answer = bfs();

    cout << answer;

    return 0;
}

int bfs(void){
    int day = 0;
    int N = arr.size();
    int M = arr[0].size();

    while (dq.size() > 0){
        deque<tmt_loc> nxt_dq;
        int initial_dq_size = dq.size();
        for (int i=0; i<initial_dq_size; i++){
            tmt_loc cur_tmt = dq.front();
            dq.pop_front();
            for (int di=0; di<4; di++){
                int nr = cur_tmt.r + dr[di];
                int nc = cur_tmt.c + dc[di];
                if (nr>=0 && nr< N && nc>=0 && nc<M){
                    if (arr[nr][nc].visit == 0 && arr[nr][nc].val == 0){
                        arr[nr][nc].visit = 1;
                        arr[nr][nc].val = 1;
                        unripe--;
                        nxt_dq.push_back({nr,nc});
                    }
                }
            }
        }
        if (nxt_dq.empty()){
            break;
        }

        day++;
        dq = nxt_dq;
    }

    if (unripe > 0){
        return -1;
    }
    else{
        return day;
    }
}