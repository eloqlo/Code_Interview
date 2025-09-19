#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <unordered_set>

using namespace std;

unsigned char _IsPrimeNumber(int n);
void GetPrimeNumbers(int N, unordered_set<string>* ptr_pns);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // INIT
    int N;
    cin >> N;
    string s;
    vector<string> ans;
    uint8_t pass_flag = 0;

    // Get Prime Number
    unordered_set<string> pns;
    pns.insert("2");
    GetPrimeNumbers(N, &pns);
    // for (const auto& elem : pns){
    //     cout << elem << '\n';
    // }

    for (int num = pow(10,N-1); num<pow(10,N); num++)   // 1000 ~ 9999
    {
        s = to_string(num);
        for (int i = s.length(); i > 0; i--)
        {   
            if (pns.find(s.substr(0,i)) == pns.end())   //TODO
            {
                pass_flag = 1;
                break;
            }
        }
        if (pass_flag == 0)
        {
            ans.push_back(s);
        }
        pass_flag = 0;
    }
    
    for (vector<string>::iterator it = ans.begin(); it != ans.end(); it++)
    {
        cout << *it << '\n';
    }
}

void GetPrimeNumbers(int N, unordered_set<string>* ptr_pns)
{
    for (int num = 2; num < pow(10,N); num++){
        if (_IsPrimeNumber(num) == 1){
            (*ptr_pns).insert(to_string(num));
        }
    }
}

unsigned char _IsPrimeNumber(int n){
    if (n==1) return 0;
    int prime_flag = 1;
    for (int i=2; i<sqrt(n)+1; i++){
        if (n%i == 0) {
            prime_flag = 0;
            break;
        }
    }
    
    if (prime_flag == 1)
        return 1;
    else
        return 0;
}