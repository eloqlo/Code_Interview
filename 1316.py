import sys

n = int(sys.stdin.readline().strip())
inputs = []

for _ in range(n):
    inputs.append(sys.stdin.readline().strip())

count = 0

for i in range(n):  # 단어별 반복
    li = []
    flag = False
    
    for j, word in enumerate(inputs[i]):  # 각 단어 가져온다.
        
        if j==0: # 첫단어 저장
            li.append(word)
        
        if word != li[len(li)-1]: # 마지막 단어랑 불일치
            for k, li_word in enumerate(li):
                if word == li_word:   # temp의 단어들이랑 비교 시작.
                    flag=True    # 기존의 bad of words 에 존재한다!
                    break
                elif k==(len(li)-1):
                    li.append(word) # 찐 새로운 단어다! li에 추가.
        if flag:    # 아닌놈이면 pass
            break
        
        if j==(len(inputs[i])-1):   # 끝까지 살아남음 -> 그룹 단어
            count += 1

print(count)

