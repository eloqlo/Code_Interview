def solution(dc_info):
    arr = [[0]*101 for _ in range(101)]
    for x,y,d,g in dc_info:
        draw_dc(arr, x,y,d,g, [])
    print(count_squares(arr))
def draw_dc(arr, x, y, first_d, g, past_d_arr):
    arr[y][x] = 1
    if g == -1:
        return
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    if len(past_d_arr)==0 and first_d!=None:
        x += dx[first_d]
        y += dy[first_d]
        arr[y][x]=1
        draw_dc(arr, x, y, None, g-1, [first_d])
    moved_d=[]
    for past_d in reversed(past_d_arr):
        d = (past_d+1)%4
        moved_d.append(d)
        x += dx[d]
        y += dy[d]
        arr[y][x] = 1
    draw_dc(arr, x,y,None, g-1,past_d_arr+moved_d)

def count_squares(arr):
    count=0
    for y in range(100):
        for x in range(100):
            count_tmp=0
            dx=[0,1,1,0]
            dy=[0,0,1,1]
            for di in range(4):
                if arr[y+dy[di]][x+dx[di]]==1:
                    count_tmp+=1
            if count_tmp==4:
                count+=1
    return count

N=int(input())
dc=[]
for _ in range(N):
    dc.append(list(map(int,input().split())))
solution(dc)