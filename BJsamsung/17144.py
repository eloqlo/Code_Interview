def solution():
    global R,C,T,arr,mj
    for _ in range(T):
        update_arr(mj)
        new_mj=[]
        for r in range(len(arr)):
            for c in range(len(arr[0])):
                if arr[r][c]>0:
                    new_mj.append((r,c,arr[r][c]))
        mj=new_mj
    result = 0
    for line in arr:
        result += sum(line)
    print(result + 2)

def print_map(arr):
    for line in arr:
        for ele in line:
            print(ele, end=' ')
        print()
def update_arr(mj):
    global arr,am,R,C
    new_arr=[[0]*C for _ in range(R)]
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    for r,c,val in mj:
        count=0
        for di in range(4):
            nr, nc = r+dr[di], c+dc[di]
            if 0<=nr<=R-1 and 0<=nc<=C-1:
                if arr[nr][nc]==-1:
                    continue
                if val//5==0:
                    break
                new_arr[nr][nc]+=val//5
                count+=1
        left_mj = val-(val//5)*count
        if left_mj > 0:
            new_arr[r][c] += left_mj
    #1
    r,c = am[0][0],am[0][1]
    tmp1 = new_arr[r][-1]
    new_arr[r] = [-1,0] + new_arr[r][1:-1]
    for r2 in range(r-1,0,-1):
        tmp2 = new_arr[r2][-1]
        new_arr[r2][-1] = tmp1
        tmp1=tmp2
    tmp2 = new_arr[0][0]
    new_arr[0] = new_arr[0][1:] + [tmp1]
    for r2 in range(1,r):
        tmp1 = new_arr[r2][0]
        new_arr[r2][0] = tmp2
        tmp2=tmp1
    #2
    r,c=am[1][0],am[1][1]
    line = new_arr[r]
    tmp1 = line[-1]
    new_arr[r] = [-1,0] + line[1:-1]
    for r2 in range(r+1,R-1):
        tmp2 = new_arr[r2][-1]
        new_arr[r2][-1] = tmp1
        tmp1 = tmp2
    tmp2=new_arr[R-1][0]
    new_arr[R-1] = new_arr[R-1][1:] + [tmp1]
    for r2 in range(R-2,r,-1):
        tmp1 = new_arr[r2][0]
        new_arr[r2][0] = tmp2
        tmp2 = tmp1
    arr = new_arr
    # return new_mj

R,C,T=map(int,input().split())
arr=[]
mj=[]
am=[]
for r in range(R):
    line = list(map(int,input().split()))
    arr.append(line)
    for c,ele in enumerate(line):
        if ele==-1:
            am.append((r,c))
        elif ele>0:
            mj.append((r,c,ele))
solution()

