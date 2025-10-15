#include <iostream>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    string foo;

    cin >> foo;
    int i;
    cin >> i;
    cout << foo[i-1];

    return 0;
}