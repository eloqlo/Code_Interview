#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> visit;      //TODO: 0으로 초기화되는거 맞나?

int solution(int n, vector<vector<int>> computers);
void dfs(vector<int> &visit, vector<vector<int>> &computers, int node);

int main(void){
    int n;
    vector<vector<int>> computers;

    cin >> n;
    vector<int> temp_line;
    for (int i=0; i<n; i++){
        
    }

    cout << solution(n, computers) << '\n';
}

int soultion(int n, vector<vector<int>> computers){
    // config
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int answer = 0;
    // Traversal
    for (int node=0; node<n; node++){
        if (visit[node] == 1)
        {
            continue;
        }
        else
        {
            answer++;
            visit[node] = 1;
            dfs(visit, computers, node);
        }
    }
    return answer;
}

/* 
visit: 방문 이력
node : 들어간 노드
action : computers 관계를 참조해 node와 연결된 노드들을 visit 처리
 */
void dfs(vector<int> &visit, vector<vector<int>> &computers, int node){
    for (int nxt_node=0; nxt_node<computers.size(); nxt_node++){
        if (visit[nxt_node]==0 && computers[node][nxt_node]==1)
        {
            visit[nxt_node] = 1;
            dfs(visit, computers, nxt_node);
        }
    }
}