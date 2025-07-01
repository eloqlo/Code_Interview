#include <vector>
#include <iostream>

using namespace std;

int main(void){
    vector<int> v;

    v.push_back(1);
    v.push_back(5);
    v.push_back(7);
    v.pop_back()
    v.push_back(8);

    cout << v << endl;

    return 0;
}