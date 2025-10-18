#include <iostream>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int N;
    cin >> N;
    string str;
    
    int answer = 0;
    cin >> str;
    for (int idx=0; idx<str.length(); idx++){
        answer += str[idx] - '0';
    }
    cout << answer;
    
    return 0;
}