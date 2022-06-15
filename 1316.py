import sys

n = int(sys.stdin.readline().strip())
inputs = []

for _ in range(n):
    inputs.append(sys.stdin.readline().strip())

count = 0

for i in range(n):  # 단어별 반복
    temp = []
    flag = False
    
    for j, word in enumerate(inputs[i]):  # 각 단어 가져온다.
        
        if flag:    # 아닌놈이면 pass
            break
        
        if j==0: # 첫단어 저장
            temp.append(word)
        
        if word == temp[len(temp)-1]:
            continue
        elif word != temp[len(temp)-1]: # 마지막 단어랑 일치x면,
            for k, temp_word in enumerate(temp):
                if word == temp_word:   # temp의 단어들이랑 비교 시작.
                    flag=True    # aabbbaa 경우임.
        
        if j==(len(inputs[i])-1):
            count += 1

print(count)