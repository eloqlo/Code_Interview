#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int calc1 = stoi(to_string(a) + to_string(b));
    int calc2 = 2*a*b;
    return (calc1 >= calc2 ? calc1 : calc2);
}