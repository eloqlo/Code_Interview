#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <typeinfo>
using namespace std;

typedef struct{
    int r;
    int c;
} loc;
typedef struct{
    int val;
    bool visit;
} arr_val;

vector<vector<arr_val>> arr;
deque<loc> dq;
deque<loc> nxt_dq;
int N,M;
loc target_loc = {N-1,M-1};
int dr[4] = {-1,1,0,0};
int dc[4] = {0,0,-1,1};
bool is_finished = false;

void arr_bfs(deque<loc> dq);
int char_to_int(char num);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    for (int r=0; r<N; r++){
        string line;
        cin >> line;
        for (char val : line){
            arr[r].push_back({char_to_int(val),false});
        }
    }
    arr[0][0].visit = true;
    
    int move = 0;
    while(dq.size() > 0){
        arr_bfs(dq);
        dq.swap(nxt_dq);
        nxt_dq.clear();

        if (dq.size()==0){
            break;
        }
        move++;
        if (is_finished){
            break;
        }
    }

    cout << move;
    return 0;
}



/* 현재 level에서 조회할 위치 dq를 받아서 arr를 업데이트해준다. */
void arr_bfs(deque<loc> dq){
    for (loc cur : dq){
        for (int di=0; di<4; di++){
            int nr = cur.r + dr[di];
            int nc = cur.c + dc[di];
            if (nr<0 || nr > N-1 || nc<0 || nc > M-1){
                continue;
            }
            if (arr[nr][nc].val == 0 || arr[nr][nc].visit == true){
                continue;
            }
            if (nr==N-1 && nc==M-1){
                is_finished = true;
            }
            arr[nr][nc].visit = true;
            nxt_dq.push_back({nr,nc});
        }
    }
}

int char_to_int(char num){
    return (int)(num - '0');
}