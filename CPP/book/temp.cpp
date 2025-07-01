#include <iostream>
#include <filesystem>
#include <string>
#include <fstream>

using namespace std;

namespace fs = filesystem;

int main() {

    // 디렉터리 생성
    fs::create_directories("MyDir");

    // 파일 생성과 쓰기
    ofstream outFile("MyDir/myFile.txt");
    outFile << "Hello~ Filesys lib!" << endl;
    outFile.close();

    // 디렉터리 탐색
    cout << "files in MyDir\n";
    for (const fs::directory_entry& entry : fs::directory_iterator("MyDir")){
        if (entry.is_regular_file()){
            cout << entry.path().filename() << endl;
        }
    }
    
    // 파일 읽기
    ifstream inFile("MyDir/myFile.txt");
    string line;
    while (getline(inFile, line)){
        cout << line << endl;
    }
    inFile.close();

    fs::remove_all("MyDir");

    return 0;
}