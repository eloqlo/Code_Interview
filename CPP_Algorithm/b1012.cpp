#include <iostream>
#include <vector>
#include <deque>
using namespace std;

typedef struct {
    int val;
    bool visit;
}place;

typedef struct{
    int r;
    int c;
} loc;

vector<vector<place>> arr;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int T;
    cin >> T ;
    vector<int> answers;

    for (int i=0; i<T; i++){
        int M, N, K, r, c;
        cin >> M >> N >> K;
        for (int i=0; i<N; i++){
            vector<place> line;
            for (int j=0; j<M; j++){
                line.push_back({0, false});
            }
            arr.push_back(line);
        }
        for (int i=0; i<K; i++){
            cin >> c >> r;
            arr[r][c].val = 1;
        }

        int answer = 0;
        int dr[4] = {-1,1,0,0};
        int dc[4] = {0,0,-1,1};
        for (int r=0; r<N; r++){
            for (int c=0; c<M; c++){
                if (arr[r][c].val == 0 || arr[r][c].visit == true) continue;
                answer++;
                deque<loc> to_visit;
                to_visit.push_back({r,c});
                arr[r][c].visit = true;
                while (!to_visit.empty()){
                    loc cur = to_visit.front();
                    to_visit.pop_front();
                    for (int di=0; di<4; di++){
                        int nr = cur.r + dr[di];
                        int nc = cur.c + dc[di];
                        if (nr<0 || nc<0 || nr>=N || nc>=M) continue;
                        if (arr[nr][nc].val == 0 || arr[nr][nc].visit == true) continue;

                        to_visit.push_back({nr,nc});
                        arr[nr][nc].visit = true;
                    }
                }
            }
        }
        answers.push_back(answer);
    }

    for(int ans : answers){
        cout << ans << endl;
    }

    return 0;
}