#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(){
    int N = 0;
    int ans = 0;
    string str;
    
    cin >> N;
    cin >> str;
    
    for(int i=0; i < str.length(); i++){
        ans += str[i] - '0';
    }

    cout << ans;
}