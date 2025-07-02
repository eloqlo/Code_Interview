#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<vector<int>> arr;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> line(N+1, 0);
    arr.push_back(line);
    for (int r=1; r<N+1; r++) {
        vector<int> line(1,0);
        int tmp = 0;

        for (int c=1; c<N+1; c++) {
            cin >> tmp;
            tmp = tmp + arr[r-1][c] + line[c-1] - arr[r-1][c-1];
            line.push_back(tmp);
        }
        arr.push_back(line);
    }
    
    /* 2-dimensional */
    for (int foo=0; foo<M; foo++) {
        int r1,c1,r2,c2;
        cin >>r1>>c1>>r2>>c2;
        int answer = arr[r2][c2] - arr[r1-1][c2] - arr[r2][c1-1] + arr[r1-1][c1-1];
        cout << answer <<"\n";
    }

    return 0;
}