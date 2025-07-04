#include <iostream>
#include <typeinfo>

using namespace std;

int main(){
    int A[1000] = {0};
    int N, SUM=0;
    int max_val = 0;
    cin >> N;

    for (int i=0; i<N; i++) {
        cin >> A[i];
        SUM += A[i];
        if (A[i] > max_val) {max_val = A[i];}
    }

    double result = (100.0*SUM)/(N*max_val);
    cout << result;
}
