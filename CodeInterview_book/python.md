# About python (Basics)

- 파이썬이 C, C++ 등과 다른 점은?
- Interpreter 언어는 뭐야?
    > 파이썬은 코드 한줄마다 기계어로 바로 번역해 실행하는 interpret 방식.
    > 이 방식은 한 문장을 번역할 때 마다 커널(os,hardware 인터페이스)이 기다려야해서 좀 느리다. 하지만 중간에 실수가 있어도 바로잡을 수 있는 장점.
- C, C++은 처음부터 끝까지 다 보고 한꺼번에 바꾸는 compile 방식
    - 잘못되었어도 수정이 힘들지만 빠르다!

## Python Compile Process
URL: https://kimwooseok.com/python/2021/06/29/python-compile/

1. 파이썬 컴파일러가 소스코드를 바이트 코드로 컴파일한다.
    > Byte Code : 소스코드를 기계어에 가까운 플랫폼 독립적인 코드로 바꾼 것. 이진코드 아니다. 시스템에서 직접 실행할 수 없다.
    > Byte Code 는 시스템의 운영체제와 상관없이, PVM에서 실행되도록 컴파일된다.
    
    1-1) 소스코드의 형식이나 명령이 올바른지 각 줄의 구문을 확인한다. 오류가 없는 경우 byte code 로 변환한다.
2. 컴파일 된 byte code 가 PVM 인터프리터로 전송된다.
    > PVM(Python Vertual Machine) : 바이트 코드를 실행하는 인터프리터, 파이썬 시스템의 일부

3. 바이트 코드는 인터프리터(PVM)에 의해 기계코드로 변환된다.
    > 기계코드 = 시스템에서 실행가능한 코드