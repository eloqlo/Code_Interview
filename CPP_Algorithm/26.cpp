#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

#define SIZE 1000

typedef struct{
    bool visit_dfs;
    bool visit_bfs;
    vector<int> connected;
}node;

void DFS(node* nd, int v){
    nd[v].visit_dfs = 1;
    cout << v << ' ';
    for (int nxt_nd : nd[v].connected){
        if (nd[nxt_nd].visit_dfs == 0){
            DFS(nd, nxt_nd);
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // initialization
    int **A = new int*[SIZE+1];
    for (int i=0; i<SIZE+1; i++)
    {
        A[i] = new int[SIZE+1];
        fill(A[i], A[i]+SIZE+1, 0);   // A[i]를 0으로 초기화. heap에 어떤 값이 있을지 모르기에 초기화 필수.
    }
    
    int n, m, v;
    cin >> n >> m >> v;
    node *nd = new node[n+1];
    int nd1, nd2;
    for (int i=0; i<m; i++)
    {
        cin >> nd1 >> nd2;
        if (A[nd1][nd2] == 0){
            nd[nd1].connected.push_back(nd2);
            nd[nd2].connected.push_back(nd1);
            A[nd2][nd1] = 1;
            A[nd1][nd2] = 1;
        }

    }
    for (int i=1; i<n+1; i++)
    {
        nd[i].visit_bfs = 0;
        nd[i].visit_dfs = 0;
        sort(nd[i].connected.begin(), nd[i].connected.end());
    }

    //DFS
    DFS(nd, v);
    cout << '\n';

    //BFS
    deque<int> dq = {v};    // 앞에서 erase 빈번히 발생 -> vector보다 메모리 분할관리하는 deque가 시간복잡도상 적절
    nd[v].visit_bfs = 1;
    while (dq.size() > 0){
        cout << dq.front() << ' ';
        for (int nxt_nd : nd[dq[0]].connected){
            if (nd[nxt_nd].visit_bfs == 0){
                nd[nxt_nd].visit_bfs = 1;
                dq.push_back(nxt_nd);
            }
        }
        dq.pop_front();
    }

    for (int i=0; i<SIZE+1; i++){
        delete[] A[i];
    }
    return 0;
}