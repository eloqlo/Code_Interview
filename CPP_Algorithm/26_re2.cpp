#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

#define SIZE 1000

typedef struct{
    int visit_bfs;
    int visit_dfs;
    vector<int> connected;
}node;

void DFS(node* nd, int v){
    nd[v].visit_dfs = 1;
    cout << v << ' ';
    for (int nxt : nd[v].connected){
        if (nd[nxt].visit_dfs == 0){
            DFS(nd, nxt);
        }
    }
}

void BFS(node* nd, int v){
    deque<int> dq = {v};
    nd[v].visit_bfs = 1;
    while (dq.size() > 0){
        int cur = dq.front();
        dq.pop_front();
        cout << cur << ' ';
        for (int nxt : nd[cur].connected){
            if (nd[nxt].visit_bfs == 0){
                nd[nxt].visit_bfs = 1;
                dq.push_back(nxt);
            }
        }
    }
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,m,v,n1,n2;
    cin >> n >> m >> v;
    node* nd = new node[n+1];
    int** A = new int*[SIZE + 1];
    for (int i=0; i<SIZE+1; i++){
        A[i] = new int[SIZE+1];
        fill(A[i], A[i]+SIZE+1, 0);
    }
    for (int i=0; i<m; i++){
        cin >> n1 >> n2;
        if (A[n1][n2] == 0){
            nd[n1].connected.push_back(n2);
            nd[n2].connected.push_back(n1);
            A[n1][n2] = 1;
            A[n2][n1] = 1;
        }
    }
    for (int i=1; i<n+1; i++){
        sort(nd[i].connected.begin(), nd[i].connected.end());
    }

    DFS(nd, v);
    cout << "\n";
    BFS(nd, v);

    for (int i=0; i<SIZE+1; i++){
        delete[] A[i];
    }
    delete[] A;
    delete[] nd;

    return 0;
}