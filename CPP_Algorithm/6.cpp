#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;  // 10,000,000
    cin >> N;
    if (N==1) {
        cout << 1; 
        return 0;
    }
    
    int st=1, ed=1, SUM=1, answer = 1;
    for (int i=2 ; i <= (N/2)+1 ; i++)
    {
        ed = i;
        SUM += ed;
        while (SUM >= N)
        {
            if (SUM == N) {answer += 1; break;}
            SUM -= st;
            st += 1;
        }
    }
    if (N==2) answer -= 1;
    cout << answer;

    return 0;
}