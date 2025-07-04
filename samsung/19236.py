"""
나는 board 중심으로 이용하며 코드 작성함. 삼성때도 그랬고.
"""

def solution(arr,fish):
    global max_score, dr, dc

    fi = arr[1][1]
    arr[1][1] = 'S'
    shark = fish[fi]
    fish[fi] = False

    move(arr,fish)

    sr,sc,sd = shark
    edible = []
    for i in range(1, 4):
        nr, nc = sr + dr[sd] * i, sc + dc[sd] * i
        if arr[nr][nc] == -1:
            break
        elif type(arr[nr][nc]) == int:
            edible.append(arr[nr][nc])
    if len(edible) == 0:
        max_score = max(max_score, 0 + (fi + 1))
        return
    else:
        for e_fi in edible:
            dfs(arr, fish, shark, e_fi, 0 + (fi + 1), 1)

    print(max_score)

def move(arr,fish):
    global dr, dc

    for fi in range(16):
        if fish[fi] == False:
            continue
        fr, fc, fd = fish[fi]
        for di in range(fd,fd+8):
            di = di%8
            nr, nc = fr+dr[di], fc+dc[di]
            if arr[nr][nc] == -1:
                continue
            if arr[nr][nc] == 'S':
                continue
            else:
                if arr[nr][nc] == '_':
                    arr[nr][nc] = fi
                    arr[fr][fc] = '_'
                    fish[fi] = [nr,nc,di]
                else:
                    tmp_fi = arr[nr][nc]
                    arr[nr][nc] = fi
                    arr[fr][fc] = tmp_fi
                    fish[tmp_fi][0] = fr
                    fish[tmp_fi][1] = fc
                    fish[fi] = [nr, nc, di]
                break

def dfs(arr_og, fish_og, shark, fi, score, depth):
    global max_score,dr,dc
    arr = [l.copy() for l in arr_og]
    fish=[]
    for l in fish_og:
        if type(l)==list:
            fish.append(l.copy())
        else:
            fish.append(l)

    # EAT
    fr, fc, fd = fish[fi]
    sr, sc, sd = shark
    arr[sr][sc] = '_'
    arr[fr][fc] = 'S'
    new_shark = [fr, fc, fd]
    fish[fi] = False

    move(arr,fish)

    edible = []
    sr, sc, sd = new_shark
    for i in range(1,4):
        nr, nc = sr+dr[sd]*i, sc+dc[sd]*i
        if arr[nr][nc]==-1:
            break
        elif type(arr[nr][nc])==int:
            edible.append(arr[nr][nc])

    if len(edible)==0:
        max_score = max(max_score, score+(fi+1))
        return
    else:
        for e_fi in edible:
            dfs(arr, fish, new_shark, e_fi, score+(fi+1), depth+1)

max_score = 0
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
arr = [[-1]*6]
fish = [0]*16
for r in range(1,5):
    arr.append([])
    arr[r].append(-1)
    l = list(map(int, input().split()))
    for i in range(0,8,2):
        fi, di = l[i]-1, l[i+1]-1
        c = i//2+1
        arr[r].append(fi)   # arr: fish index
        fish[fi] = [r,c,di]
    arr[r].append(-1)
arr.append([-1]*6)
solution(arr,fish)