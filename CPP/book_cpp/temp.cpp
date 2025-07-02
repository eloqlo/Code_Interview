#include <iostream>
using namespace std;

template <typename T1, typename T2>
class data_package {
    public:
        template <typename T3>
        class nested_class_data_package{
            public:
                nested_class_data_package(T3 data) : nested_class_data(data){}
                T3 get_element() {return nested_class_data;}
                T3 nested_class_data;
        };

        template <typename T4>
        class nested_class {
            public:
                nested_class(T4 data) : nested_class_data(data){}
                void print_out_element(){
                    cout << "중첩 클래스 데이터: " << nested_class_data << endl;
                }
            private:
                T4 nested_class_data;
        };
        
        data_package(T1 first, T2 second) : first(first), second(second), internal_data(second) {}

        void print_out_element() {
            cout << "첫 번째 요소: " << first << ", 두 번째 요소: " << second << endl;
            cout << "중첩 클래스 요소: " << internal_data.get_element() << endl;
        }
    
    private:
        T1 first;
        T2 second;
        nested_class_data_package<T2> internal_data;        // 모름: main에서 "data_package<string, int> template_inst1("문자열", 10);"을 통해 생성자가 인수를 넘겨받고, "data_package(T1 first, T2 second) : first(first), second(second), internal_data(second) {}" 부분에서 internal_data(10) 이렇게 넘겨받잖아, 이 때 internal_data는 객체인데 어떻게 함수처럼 10을 받을 수있는건지 동작이 이해가 안돼
};

int main() {
    data_package<string, int> template_inst1("문자열", 10);
    data_package<string, int>::nested_class<int> template_inst2(500);

    cout << "중첩 클래스 첫 번째 범례" << endl;
    template_inst1.print_out_element();

    cout << endl << "중첩 클래스 두 번째 범례" << endl;
    template_inst2.print_out_element();
    return 0;
}