#include <iostream>
#include <vector>
#include <deque>
using namespace std;


void solution(){
    int answer = 0;
    int N, node_ed;
    cin >> N;
    vector<int> arr;
    arr.push_back(0);
    vector<int> visit(N+1, false);

    for (int node_st=1; node_st<N+1; node_st++){
        cin >> node_ed;
        arr.push_back(node_ed);
    }


    for (int node=1; node<N+1; node++){
        if (visit[node]) continue;

        answer++;
        visit[node] = true;
        int nxt_node = arr[node];
        while(!visit[nxt_node]){
            visit[nxt_node] = true;
            nxt_node = arr[nxt_node];
        }
    }

    cout << answer << '\n';
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    for (int tc=0; tc<T; tc++){
        solution();
    }
}