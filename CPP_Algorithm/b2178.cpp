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
int dr[4] = {-1,1,0,0};
int dc[4] = {0,0,-1,1};
bool is_finished = false;

void arr_bfs(deque<loc> &dq);
int char_to_int(char num);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> N >> M;
    vector<arr_val> line_vec;
    for (int r=0; r<N; r++){
        string line;
        cin >> line;
        for (char val : line){
            line_vec.push_back({char_to_int(val),false});
        }
        arr.push_back(line_vec);
        line_vec.clear();
    }
    
    arr[0][0].visit = true;
    dq.push_back({0,0});

    int move = 1;
    while(!dq.empty()){
        arr_bfs(dq);
        dq.swap(nxt_dq);
        nxt_dq.clear();

        move++;
        if (is_finished) break;
        if (dq.empty()) break;
    }

    cout << move << endl;
    return 0;
}



/* 현재 level에서 조회할 위치 dq를 받아서 arr를 업데이트해준다. */
void arr_bfs(deque<loc> &dq){
    for (loc cur : dq){
        for (int di=0; di<4; di++){
            int nr = cur.r + dr[di];
            int nc = cur.c + dc[di];
            if (nr<0 || nr >= N || nc<0 || nc >= M) continue;
            if (arr[nr][nc].val == 0 || arr[nr][nc].visit == true) continue;
            arr[nr][nc].visit = true;
            if (nr==N-1 && nc==M-1) is_finished = true;
            nxt_dq.push_back({nr,nc});
        }
        if (is_finished) break;
    }
}

int char_to_int(char num){
    return (int)(num - '0');
}