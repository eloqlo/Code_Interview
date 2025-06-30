/*
1. counter[MAX_NUM] 배열이 너무 커서 stack overflow 발생
    : 런타임에서 크기가 결정되는 지역변수기에, stack에 할당됨
    : 대부분의 시스템에서 stack 메모리의 크기는 1MB ~ 8MB 정도임.
    : segmentation fault(메모리 크기 초과 참조) 발생 가능성 큼
-> counter을 전역으로 옮겨서 Bss section에 할당하기
-> new를 이용해 동적 할당. heap에 저장됨.
-> vector 사용 (런타임 크기 배열을 정식으로 지원! 내부적으로 new를 사용해)

*/

#define MAX_NUM 1000000
#include <iostream>
#include <vector>

using namespace std;

vector<int> counter(MAX_NUM);     // 4MB

int main(){
    int N;
    cin >> N;
    vector<int> li(N);
    for(int i=0; i<N; i++){
        int tmp;
        cin >> tmp;
        li[i] = tmp;
    }

    /*Count Sort*/
    for(int i=0; i<N; i++){
        // cout << counter[i];     //! DEBUG
        counter[li[i]]++;
    }

    cout << endl;
    vector<int> answer(N);
    int idx=0;
    for(int i=0; i<MAX_NUM; i++){
        cout << i << "\n";
    }
    
    return 0;
}