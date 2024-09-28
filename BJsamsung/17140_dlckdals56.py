"""
1. 2차원 배열 대각화 방법
2. 2가지 정렬기준으로 정렬 하는 법
+ dictionary.itmes()
"""


r, c, k = map(int, input().split())

r -= 1
c -= 1

game = []

for i in range(3):
    game.append(list(map(int, input().split())))


def toString():
    for i in game:
        for j in i:
            print(j, end='')
        print()
    print('----')


def R():
    maxs = 0
    for i in range(len(game)):
        dict = {}
        for j in game[i]:
            if j == 0:
                continue
            if j not in dict:
                dict[j] = 1
            else:
                dict[j] += 1
        t = sorted(dict.items(), key=lambda x: (x[1], x[0]))
        temp = []
        for x, y in t:
            temp.append(x)
            temp.append(y)

        game[i] = temp[:100]
        maxs = max(maxs, len(game[i]))

    for i in range(len(game)):
        game[i] = game[i] + [0] * (maxs - len(game[i]))


idx = 0

while 1:

    if r <= len(game) - 1 and c <= len(game[0]) - 1:
        if game[r][c] == k:
            print(idx)
            break

    idx += 1

    if idx > 100:
        print(-1)
        break

    if len(game) >= len(game[0]):
        R()

    else:
        game = list(zip(*game))
        R()
        game = list(zip(*game))

