/*
이차원 vector 배열

*/

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<vector<int>> arr;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> first_line(N+1, 0);
    arr.push_back(first_line);
    for (int r = 1 ; r < N+1 ; r++) {
        vector<int> line(N+1, 0);
        arr.push_back(line);
        int tmp;
        for (int c=1; c<N+1; c++) {
            cin >> tmp;
            arr[r][c] = tmp + arr[r-1][c] + arr[r][c-1] - arr[r-1][c-1];
        }
    }
    
    /* 2-dimensional */
    for (int foo=0; foo<M; foo++) {
        int r1,c1,r2,c2;
        cin >>r1>>c1>>r2>>c2;
        cout << arr[r2][c2] - arr[r1-1][c2] - arr[r2][c1-1] + arr[r1-1][c1-1] << "\n";
    }

    return 0;
}