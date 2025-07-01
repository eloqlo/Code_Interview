#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


struct Person{
    string name;
    int age;
    float height;
    float weight;
};

void print_person_all(vector<Person>& vec){
    for (vector<Person>::iterator it = vec.begin(); it!=vec.end(); it++){
        cout << "이름: " << it->name << "\t" << "나이: " << it->age << ", "
        << "키: " << it->height << ", 몸무게: " << it->weight << endl;
    }
}

int main(){
    Person p[2] = {
        {"Brain", 24, 173, 75},
        {"Alice", 28, 160, 58}
    };

    vector<Person> from_vector;
    from_vector.push_back(p[0]);
    from_vector.push_back(p[1]);


    cout << "----from_vector-----" << endl;
    print_person_all(from_vector);
    cout << endl;

    vector<Person> to_vector;
    copy(from_vector.begin(), from_vector.end(), back_inserter(to_vector));

    
    cout << "----to_vector-----" << endl;
    print_person_all(to_vector);
    cout << endl;

    from_vector[0].name = "Lee";
    from_vector[0].weight = 100;


    cout << "----from_vector-----" << endl;
    print_person_all(from_vector);
    cout << endl;
    cout << "----to_vector-----" << endl;
    print_person_all(to_vector);
    cout << endl;


    return 0;
}