#include <iostream>
#include <vector>

using namespace std;

typedef struct{
    int visit;
    vector<int> connected;
} node;

void dfs(int idx, node* nd){
    nd[idx].visit = 1;
    for (int i=0; i<nd[idx].connected.size(); i++){
        if (nd[nd[idx].connected[i]].visit == 0){
            dfs(nd[idx].connected[i], nd);
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n,m,u,v;
    cin >> n >> m;
    node* nd = new node[n+1];
    for (int i=0; i<m; i+=1){
        cin >> u >> v;
        nd[u].connected.push_back(v);
        nd[v].connected.push_back(u);
    }

    int answer = 0;
    for (int i=1; i<n+1; i++){
        if (nd[i].visit==0){
            dfs(i, nd);
            answer++;
        }
    }
    cout << answer << '\n';
}