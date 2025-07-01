def solution(arr):
    global r,c,k
    count=0
    while 1:
        if r<len(arr) and c<len(arr[0]):
            if arr[r][c]==k:
                print(count)
                break
        count+=1
        if count==101:
            print(-1)
            break
        arr = update_arr(arr)

def update_arr(arr):
    if len(arr)>=len(arr[0]):
        return arr_compute_row(arr)
    else:
        arr = list(zip(*arr))
        arr = arr_compute_row(arr)
        return list(zip(*arr))

def arr_compute_row(arr):
    max_len=0
    new_arr=[]
    for line in arr:
        counter=[0]*101
        for ele in line:
            counter[ele]+=1
        tmp_line=[]
        for num,val in enumerate(counter):
            if num==0 or val==0:
                continue
            tmp_line.append((num,val))
        tmp_line = sorted(tmp_line, key=lambda x:(x[1],x[0]))
        new_line=[]
        for num,val in tmp_line:
            new_line.append(num)
            new_line.append(val)
        max_len = max(max_len,len(new_line))
        new_arr.append(new_line)
    for r in range(len(new_arr)):
        new_arr[r] = new_arr[r] + [0]*(max_len-len(new_arr[r]))
    return new_arr


r, c, k = map(int, input().split())
r -= 1
c -= 1
arr = [list(map(int, input().split())) for line in range(3)]
solution(arr)