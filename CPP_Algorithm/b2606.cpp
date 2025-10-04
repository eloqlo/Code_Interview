#include <iostream>
#include <deque>
#include <vector>
using namespace std;

/* 자료구조: linked list, 알고리즘: bfs */

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int num_computers, num_connections, com1, com2;
    cin >> num_computers >> num_connections;
    vector<vector<int>> connections(num_computers + 1);
    vector<bool> visit(num_computers, false);
    visit[1] = true;
    for (int i=0; i<num_connections; i++){
        cin >> com1 >> com2;
        connections[com1].push_back(com2);
        connections[com2].push_back(com1);
    }
    
    int answer = 0;
    deque<int> dq;
    deque<int> nxt_dq;
    dq.push_back(1);    // start at node 1
    while(!dq.empty()){
        for (int node : dq){
            for (int tmp_node : connections[node]){
                if (visit[tmp_node] == true) continue;
                answer++;
                visit[tmp_node] = true;
                nxt_dq.push_back(tmp_node);
            }
        }
        dq.swap(nxt_dq);
        nxt_dq.clear();
    }
    
    cout << answer << endl;

    return 0;
}