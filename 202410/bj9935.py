import sys

def solution():

    word = sys.stdin.readline().strip()
    chk = sys.stdin.readline().strip()
    l = len(chk)
    nxt_word = []

    for idx in range(len(word)):
        nxt_word.append(word[idx])

        if ''.join(nxt_word[-l:]) == chk:
            for _ in range(l):
                nxt_word.pop()
    word = ''.join(nxt_word)

    if len(word)==0:
        print("FRULA")
    else:
        print(word)

solution()