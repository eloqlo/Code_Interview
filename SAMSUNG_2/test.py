diff = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북동남서

cur_di=1
A_new = [[0,1,0,0,0],
         [0,0,0,0,1],
         [0,6,0,0,0],
         [1,0,0,0,0]]
CUR_SIZE = 17
cr,cc = 0,1
N,M = 4,5

dr,dc = diff[cur_di]
for co in range(1,max(N,M)):
    nr = cr + dr*co
    nc = cc + dc*co
    if 0<=nr<N and 0<=nc<M:
        if A_new[nr][nc] == 6:
            break
        elif A_new[nr][nc] == 0:
            A_new[nr][nc] = '#'
            CUR_SIZE -= 1
    else:
        break

for l in A_new:
    for e in l:
        print(e, end= ' ')
    print()
print("CUR_SIZE ",CUR_SIZE)