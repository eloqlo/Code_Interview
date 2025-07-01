#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    float answer = 0;
    
    float num2_flt = num2;
    
    answer = num1/num2_flt;
    answer = answer*1000;
    
    int ans = answer;
    return ans;
}

/*
    내가 몰랐던건 계산시 자료형이 구체적으로 어떻게 작동하는지 였던것같다.
*/