# 지능형 기차 2
people = 0
max_people = 0
for _ in range(10):
    o, i = map(int, input().split())
    people += i
    people -= o
    
    if people>max_people:
        max_people = people

print(max_people)