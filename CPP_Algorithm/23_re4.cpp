#include <iostream>
#include <vector>

using namespace std;

typedef struct{
    int visit;
    vector<int> near;
}node;

void dfs(int num, node* nd){
    nd[num].visit = 1;
    for (vector<int>::const_iterator it = nd[num].near.cbegin(); it != nd[num].near.cend(); it++){
        if (nd[*it].visit==0)
            dfs(*it, nd);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N,M,u,v;
    cin >> N >> M;
    node* nd = new node[N+1];
    for (int i=0; i<M; i++){
        cin >> u >> v;
        nd[u].near.push_back(v);
        nd[v].near.push_back(u);
    }

    int answer = 0;
    for (int i=1; i<N+1; i++){
        if (nd[i].visit == 0){
            answer++;
            dfs(i, nd);
        }
    }

    cout << answer;
}