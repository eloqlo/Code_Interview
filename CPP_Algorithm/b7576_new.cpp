#include <iostream>
#include <vector>
#include <deque>
using namespace std;

typedef struct{
    int r;
    int c;
} loc;
typedef struct{
    int val;
    bool visit;
} tmt;

int dr[4] = {1,-1,0,0};
int dc[4] = {0,0,1,-1};
int M, N;
vector<vector<tmt>> arr;
deque<loc> dq;
int space_cnt = 0;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // INITIALIZATION
    /* arr, dq */
    cin >> M >> N;
    int val;
    for (int r=0; r<N; r++)
    {
        vector<tmt> line;
        for (int c=0; c<M; c++)
        {
            cin >> val;
            line.push_back({val,false});
            if (val == 1)
            {
                dq.push_back({r,c});
                line[c].visit = true;
            }
            else if (val == 0)
                space_cnt++;
        }
        arr.push_back(line);
    }

    if (space_cnt == 0)
    {
        cout << 0;
        return 0;
    }

    // ALGORITHM
    int day = 0;
    while(dq.size() > 0)
    {
        deque<loc> nxt_dq;
        for(loc tmt_loc : dq)
        {
            for (int di=0; di<4; di++)
            {
                int nr = tmt_loc.r + dr[di];
                int nc = tmt_loc.c + dc[di];
                if (nr<0 || nr>=N || nc<0 || nc>=M)
                    continue;
                if (arr[nr][nc].val != 0 || arr[nr][nc].visit)
                    continue;
                
                arr[nr][nc].visit = true;
                arr[nr][nc].val = 1;
                nxt_dq.push_back({nr,nc});
                space_cnt--;
            }
        }
        if (nxt_dq.size() > 0)
        {
            day++;
        }
        dq.swap(nxt_dq);
    }

    if (space_cnt==0)
        cout << day;
    else   
        cout << -1;
    return 0;
}