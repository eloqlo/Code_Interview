import sys

word = sys.stdin.readline().strip().lower()

vocab = {}
for i in word:
    if i in vocab:
        vocab[i] += 1   # 있으면 1 덧셈
    else:
        vocab[i] = 1    # 없으면 추가

val = list(vocab.values())
max_val = max(val)

count = 0
for k in val:
    if k==max_val: count+=1

if count>1:
    print('?')
else:
    max_key = max(vocab, key=vocab.get)
    print(max_key.upper())