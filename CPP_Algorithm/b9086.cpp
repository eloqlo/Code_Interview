#include <iostream>
#include <string>
using namespace std;

int main(){
    int T;
    cin >> T;
    for (int i=0; i<T; i++){
        string tmp;
        cin >> tmp;
        cout << tmp[0] << tmp[tmp.length()-1] << endl;
    }
    return 0;
}