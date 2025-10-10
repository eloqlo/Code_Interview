#include <iostream>
#include <deque>
#include <vector>
using namespace std;

typedef struct{
    int parent;
    // int node;
    vector<int> children;
} node;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, target1, target2, m, p, c;
    cin >> n;
    cin >> target1 >> target2;
    cin >> m;
    
    node vocab[n+1];
    for (int i=1; i<n; i++){
        vocab[i].parent = -1;
    }
    for (int i=0; i<m; i++){
        cin >> p >> c;
        vocab[p].children.push_back(c);
        vocab[c].parent = p;
    }

    /* traverse */
    bool visited[n+1] = {false};
    visited[target1] = true;
    vector<int> nxt_visit;
    vector<int> nodes = {target1};
    int count = 0;
    bool end_flag = false;
    while(!nodes.empty()) {
        count++;
        for (int cur_node : nodes){
            int parent = vocab[cur_node].parent;
            if (visited[parent]==false && parent != -1){
                if (parent == target2){
                    end_flag = true;
                    break;
                }
                nxt_visit.push_back(parent);
                visited[parent] = true;
            }
            if (end_flag) break;
            for (int nxt_node : vocab[cur_node].children){
                if (nxt_node == target2) {
                    end_flag=true;
                    break;
                }
                if (!visited[nxt_node]){
                    nxt_visit.push_back(nxt_node);
                    visited[nxt_node] = true;
                }
            }
        }
        if (end_flag) break;
        nodes.swap(nxt_visit);
        nxt_visit.clear();
    }

    if (nodes.empty()){
        cout << -1;
    } else{
        cout << count;
    }
    return 0;
}