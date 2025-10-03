#include <iostream>
#include <vector>
#include <deque>
using namespace std;

typedef struct{
    int r;
    int c;
}tomatto_location;

deque<tomatto_location> tomatto;
vector<vector<int>> arr;
int dr[4] = {-1,1,0,0};
int dc[4] = {0,0,-1,1};
int count_blank = 0;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // Set <arr, tomatto>
    int N, M, tmp_val;
    cin >> M >> N;
    for (int r=0; r<N; r++){
        vector<int> line;
        for (int c=0; c<M; c++){
            cin >> tmp_val;
            if (tmp_val==1){
                tomatto.push_back({r,c});
            }
            if (tmp_val==0){
                count_blank++;
            }
            line.push_back(tmp_val);
        }
        arr.push_back(line);
    }

    // BFS
    int day = 0;
    while (tomatto.size() > 0){
        deque<tomatto_location> nxt_tomatto;
        for (tomatto_location cur_tmt : tomatto){
            for (int di=0; di<4; di++){
                int nr = cur_tmt.r + dr[di];
                int nc = cur_tmt.c + dc[di];
                if (nr<0 || nc<0 || nr>=N || nc>=M){
                    continue;
                }
                if (arr[nr][nc]!=0){
                    continue;
                }
                arr[nr][nc] = 1;
                count_blank--;
                nxt_tomatto.push_back({nr,nc});
            }
        }
        tomatto = nxt_tomatto;
        if(tomatto.size() > 0){
            day++;
        }
    }
    
    if (count_blank > 0){
        day = -1;
    }
    cout << day;
    return 0;
}