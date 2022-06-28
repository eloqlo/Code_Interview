N = int(input())
word = []

for _ in range(N):
    word.append(input())

word = list(set(word))  # kill 중복
word.sort(key=lambda x : (len(x),x))    #  len(x)를 기준으로 정렬하고 같을 경우 x를 기준으로 정렬하기

print("\n".join(word))  # 표현법