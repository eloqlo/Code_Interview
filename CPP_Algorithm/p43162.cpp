#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> visit;      //TODO: 0으로 초기화되는거 맞나?

int solution(int n, vector<vector<int>> computers);
void dfs(vector<int> &visit, int node);

int main(void){

    int n;
    vector<vector<int>> computers;

    cout << solution(n, computers) << '\n';
}

int soultion(int n, vector<vector<int>> computers){
    // config
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    
    int answer = 0;
    // Traversal
    for (int i=0; i<n; i++){
        
    }



    return answer;
}

/* 
visit: 방문 이력
node : 들어간 노드
 */
void dfs(vector<int> &visit, int node){

}