import sys

word = sys.stdin.readline().strip().lower()

vocab = {}
for i in word:
    if i in vocab:
        vocab[i] += 1   # 있으면 1 덧셈
    else:
        vocab[i] = 1    # 없으면 추가

val = list(vocab.values())

if len(set(val))!=len(val):
    print('?')
else:
    max_key = max(vocab, key=vocab.get)
    print(max_key)