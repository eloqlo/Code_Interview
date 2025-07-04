def solution(debug):
    global cmd, score, green, blue
    for t,r,c in cmd:
        # 기준점
        if t==1:
            gr, gc = 1, c
            br, bc = 1, r
        elif t==2:
            gr, gc = 1, c   # gc+1 같이 따질거
            br, bc = 1, r   # br-1 추가 예정
        elif t==3:
            gr, gc = 1, c   # gr-1 추가 예정
            br, bc = 1, r   # bc+1 추가 예정

        update_green(t, gr, gc, debug)
        update_blue(t, br, bc, debug)

    count=0
    for r in range(6):
        count += sum(green[r]) + sum(blue[r])
    return score, count

def update_green(t, r, c, debug):
    global score, green
    nr=r
    for foo in range(6):
        nr = nr+1
        if t==1:
            if nr>len(green)-1:
                green[nr-1][c] = 1
                break
            elif green[nr][c]==0:
                continue
            else:
                green[nr-1][c]=1
                break
        elif t==2:
            if nr>len(green)-1:
                green[nr - 1][c] = 1
                green[nr - 1][c + 1] = 1
                break
            elif green[nr][c]+green[nr][c+1]==0:
                continue
            else:
                green[nr-1][c] = 1
                green[nr-1][c+1] = 1
                break
        elif t==3:
            if nr > len(green)-1:
                green[nr - 2][c] = 1
                green[nr-1][c] = 1
                break
            elif green[nr][c] + green[nr-1][c] == 0:
                continue
            else:
                green[nr-2][c] = 1
                green[nr-1][c] = 1
                break

    # check complete row
    new_green=[]
    new_r_counter=0
    for pop_r in range(6):
        if sum(green[pop_r])==4:
            score+=1
            new_r_counter+=1
        else:
            new_green.append(green[pop_r])
    new_green = [[0]*4 for _ in range(new_r_counter)] + new_green

    # check row 0, row 1
    if sum(new_green[0])>0:
        new_green.pop()
        new_green = [[0]*4] + new_green
    if sum(new_green[1])>0:
        new_green.pop()
        new_green = [[0] * 4] + new_green
    green = new_green

def update_blue(t, r, c, debug):
    global score, blue
    nr=r
    for foo in range(6):
        nr = nr+1
        if t==1:
            if nr>len(blue)-1:
                blue[nr - 1][c] = 1
                break
            elif blue[nr][c]==0:
                continue
            else:
                blue[nr-1][c]=1
                break
        elif t==2:
            if nr>len(blue)-1 :
                blue[nr-2][c] = 1
                blue[nr-1][c] = 1
                break
            elif blue[nr][c]+blue[nr-1][c]==0:
                continue
            else:
                blue[nr-2][c] = 1
                blue[nr-1][c] = 1
                break
        elif t==3:
            if nr > len(blue)-1:
                blue[nr - 1][c] = 1
                blue[nr - 1][c + 1] = 1
                break
            elif blue[nr][c] + blue[nr][c+1] == 0:
                continue
            else:
                blue[nr-1][c] = 1
                blue[nr-1][c+1] = 1
                break

    # check complete row
    new_blue=[]
    new_r_counter=0
    for pop_r in range(6):
        if sum(blue[pop_r])==4:
            score+=1
            new_r_counter+=1
        else:
            new_blue.append(blue[pop_r])
    new_blue = [[0]*4 for _ in range(new_r_counter)] + new_blue

    # check row 0, row 1
    if sum(new_blue[0])>0:
        new_blue.pop()
        new_blue = [[0]*4] + new_blue
    if sum(new_blue[1])>0:
        new_blue.pop()
        new_blue = [[0]*4] + new_blue
    blue = new_blue

# GOGO
N = int(input())
cmd = [list(map(int,input().split())) for _ in range(N)]
score = 0
green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]
DEBUG = False
s,c = solution(DEBUG)
print(s)
print(c)