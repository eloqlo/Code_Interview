#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <algorithm>
using namespace std;

typedef struct{
    int val;
    bool visit;
}arr_val;
typedef struct{
    int r;
    int c;
}arr_loc;

vector<vector<arr_val>> arr;
int N;

int bfs(int r, int c){
    int count = 1;
    int dr[4] = {-1,1,0,0};
    int dc[4] = {0,0,-1,1};

    deque<arr_loc> dq;
    dq.push_back({r,c});
    arr[r][c].visit = true;
    while(!dq.empty()){
        arr_loc cur_loc;
        cur_loc = dq.front();
        dq.pop_front();
        for (int di=0; di<4; di++){
            int nr = cur_loc.r + dr[di];
            int nc = cur_loc.c + dc[di];
            if (nr<0 || nc<0 || nr>=N || nc>=N) continue;
            if (arr[nr][nc].val==0 || arr[nr][nc].visit==true) continue;

            count++;
            arr[nr][nc].visit = true;
            dq.push_back({nr,nc});
        }
    }
    return count;
}

int ctoi(char c){
    return c - '0';
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++){
        vector<arr_val> av;
        string buf;
        cin >> buf;
        for (int j=0; j<N; j++){
            av.push_back({ctoi(buf[j]), false});
        }
        arr.push_back(av);
    }

    vector<int> house_count;
    int total_count = 0;
    for (int r=0; r<N; r++){
        for (int c=0; c<N; c++){
            if (arr[r][c].val==1 && arr[r][c].visit == false){
                house_count.push_back(bfs(r,c));
                total_count++;
            }
        }
    }
    sort(house_count.begin(), house_count.end());

    cout << total_count << endl;
    for (int ans : house_count){
        cout << ans << '\n';
    }

    return 0;
}