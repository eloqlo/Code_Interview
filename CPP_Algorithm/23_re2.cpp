// https://www.acmicpc.net/problem/11724
#include <iostream>
#include <vector>

using namespace std;

typedef struct{
    int visit = 0;
    vector<int> connected;
} graph;

void dfs(int num, graph* graph_ref){
    graph_ref[num].visit = 1;
    for (int i=0; i<graph_ref[num].connected.size(); i++){
        if (graph_ref[graph_ref[num].connected[i]].visit == 0){
            dfs(graph_ref[num].connected[i], graph_ref);
        }
    }
    // for (vector<int>::const_iterator it = graph_ref[num].connected.cbegin(); it != graph_ref[num].connected.cend(); it++){
    //     if(graph_ref[*it].visit == 0){
    //         dfs(*it, graph_ref);
    //     }
    // }
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // INPUTS
    int N,M;
    cin >> N >> M;
    // vector<graph> graph_vec(N+1);
    graph* graph_vec = new graph[N+1];
    int u,v;
    for (int i = 0; i < M; i++){
        cin >> u >> v;
        graph_vec[u].connected.push_back(v);
        graph_vec[v].connected.push_back(u);
    }

    // DFS
    int answer = 0;
    for (int num = 1; num < N+1; num++){
        if (graph_vec[num].visit == 1){
            continue;
        }
        answer += 1;
        dfs(num, graph_vec);   // visit every connected nodes !
    }

    cout << answer;
    delete[] graph_vec;
}