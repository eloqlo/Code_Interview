#include <string>
#include <vector>

using namespace std;

int global_answer = 0;
int global_target;

void dfs(vector<int> &numbers, int pos, int prev);

int solution(vector<int> numbers, int target) {
    global_target = target;
    int start_pos = 0;
    int start_num = 0;
    
    dfs(numbers, start_pos, start_num);
    return global_answer;
}

void dfs(vector<int> &numbers, int pos, int prev){
    if (pos == numbers.size()){
        if (prev == global_target)
            global_answer++;
    }
    else{
        dfs(numbers, pos+1, prev - numbers[pos]);
        dfs(numbers, pos+1, prev + numbers[pos]);
    }
}