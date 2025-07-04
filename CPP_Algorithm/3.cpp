#include <iostream>
#include <vector>
using namespace std;

vector<int> SUM = {0};

int main() {
    int N, M, st, ed, tmp;
    cin >> N >> M;

    for (int i=0; i<N; i++) {
        cin >> tmp;
        SUM.push_back(tmp + SUM.at(i));
    }

    for (int i=0; i<M; i++) {
        cin >> st >> ed;
        cout << SUM.at(ed) - SUM.at(st-1) << "\n";
    }
    
    return 0;
}   