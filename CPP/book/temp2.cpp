#include <random>
#include <iostream>
#include <chrono>

using namespace std;

int main(){

    // auto curTime = chrono::system_clock::now();
    // auto duration = curTime.time_since_epoch();
    // auto millis = chrono::duration_cast<chrono::microseconds>(duration).count();
    // mt19937_64 mt_rand(millis);

    random_device rng;

    for (int i=0; i<10; i++){
        auto result = rng();
        cout << result << endl;
        // cout << mt_rand() << endl;
    }

    return 0;
}