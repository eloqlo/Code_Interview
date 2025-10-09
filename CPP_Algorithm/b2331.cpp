#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <string>
using namespace std;

int get_next(int num, int P){
    string tmp = to_string(num);
    int ret = 0;
    for (char tt : tmp){
        int val = 1;
        for(int i=0; i<P; i++){
            val *= tt - '0';
        }
        ret += val;
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int A, P;
    int count = 0;
    vector<int> D;
    unordered_map<int, bool> visit;
    cin >> A >> P;
    int answer = 0;

    while(visit.find(A) == visit.end()) {
        count++;
        visit[A] = true;
        D.push_back(A);
        A = get_next(A, P);
        if (visit.find(A) != visit.end()){
            /* C Style */
            for (int i=0; i<D.size(); i++){
                if (D[i] == A){
                    answer = i;
                    break;
                }
            }
            break;
        }
    }
    cout << answer;
}