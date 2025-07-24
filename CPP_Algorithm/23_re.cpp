#include <iostream>
#include <vector>

using namespace std;

typedef struct {
    int idx;
    int visit;
    vector<int> connected;
} node;

void dfs(int idx, vector<node> &graph){
    if (graph[idx].visit == 0){
        graph[idx].visit = 1;
        for (vector<int>::const_iterator it = graph[idx].connected.cbegin(); it != graph[idx].connected.cend(); it++){
            if (graph[*it - 1].visit == 0)
                dfs(*it - 1, graph);
        }
    }
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // initializing
    int N, M;
    vector<node> graph;
    cin >> N >> M;
    for (int idx=1; idx<N+1; idx++){
        node nd = {idx, 0};
        graph.push_back(nd);
    }
    int u, v;
    for (int i=0; i<M; i++){
        cin >> u >> v;
        graph[u-1].connected.push_back(v);
        graph[v-1].connected.push_back(u);
    }

    // traverse(DFS)
    int answer = 0;
    for (int idx=0; idx<N; idx++){
        if (graph[idx].visit == 0){
            dfs(idx, graph);
            answer += 1;
        }
    }

    cout << answer;

}