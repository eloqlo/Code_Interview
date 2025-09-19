#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

#define SIZE 1000

typedef struct{
    int visit_dfs;
    int visit_bfs;
    vector<int> connected;
}node;

void DFS(node* nd, int v){
    nd[v].visit_dfs = 1;
    cout << v << ' ';
    for (int i : nd[v].connected){
        if (nd[i].visit_dfs == 0){
            DFS(nd, i);
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,m,v,n1,n2;
    // int CHK[SIZE+1][SIZE+1] = {0,};
    int** CHK = new int*[SIZE+1];
    for (int i=0; i<SIZE+1; i++){
        CHK[i] = new int[SIZE+1];
        fill(CHK[i], CHK[i]+SIZE+1, 0);
    }
    
    // initialize nodes
    cin >> n >> m >> v;
    node* graph = new node[n+1];
    for (int i=0; i<m; i++){
        cin >> n1 >> n2;
        if (CHK[n1][n2] == 0){
            CHK[n1][n2] = 1;
            CHK[n2][n1] = 1;
            graph[n1].connected.push_back(n2);
            graph[n2].connected.push_back(n1);
        }
    }

    // sort nodes
    for (int i=1; i<n+1; i++){
        sort(graph[i].connected.begin(), graph[i].connected.end());
    }

    // DFS
    DFS(graph, v);
    cout << "\n";
    
    // BFS
    deque<int> dq = {v};
    graph[v].visit_bfs = 1;
    while (dq.size() > 0){
        cout << dq.front() << ' ';
        for (int nxt_v : graph[dq.front()].connected){
            if (graph[nxt_v].visit_bfs == 0){
                graph[nxt_v].visit_bfs = 1;
                dq.push_back(nxt_v);
            }
        }
        dq.pop_front();
    }

    return 0;
}