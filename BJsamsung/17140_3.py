def solution(arr):
    global r, c, k
    count = 0
    for iteration in range(101):
        if r<len(arr) and c<len(arr[0]):
            if arr[r][c] == k:
                return count
        if iteration==100:
            break
        count += 1
        arr = get_new_arr(arr)
    return -1

def get_new_arr(arr):
    R = len(arr)
    C = len(arr[0])
    if R>=C:
        # row-wise
        new_arr = []
        max_line_len = 0
        for line in arr:
            new_line = get_new_line(line)
            max_line_len = max(max_line_len,len(new_line))
            new_arr.append(new_line)
        for idx in range(len(new_arr)):
            new_arr[idx] = new_arr[idx] + [0]*(max_line_len-len(new_arr[idx]))
    else:
        # col-wise
        new_dig_arr = []
        max_line_len = 0
        for col in zip(*arr):
            new_col = get_new_line(list(col))
            max_line_len = max(max_line_len, len(new_col))
            new_dig_arr.append(new_col + [0]*(100-len(new_col)))
        new_arr = []
        for iteration, new_row in enumerate(zip(*new_dig_arr)):
            if iteration==max_line_len:
                break
            new_arr.append(list(new_row))
    return new_arr


def get_new_line(line):
    counter = [0]*101
    for num in line:    # O(100)
        counter[num] += 1
    sorting_line=[]
    for num,freq in enumerate(counter):     # O(100)
        if num==0 or freq==0:
            continue
        if len(sorting_line)==0:
            sorting_line.append((freq,num))
            continue
        sorting_line = binary_search(sorting_line, freq, num)   # less than 8
    sorted_line = []
    for idx, (freq, num) in enumerate(sorting_line):   # O(100)
        if idx == 50:
            break
        sorted_line.append(num)
        sorted_line.append(freq)
    return sorted_line[:100]

def binary_search(sorting_line, freq, num):
    st=0
    ed=len(sorting_line)-1
    pos=None
    for _ in range(len(sorting_line)+2):
        if st>ed:
            pos=max(st,ed)
            break
        mid = (st+ed)//2
        if sorting_line[mid][0]<=freq:
            st = mid+1
        elif sorting_line[mid][0]>freq:
            ed = mid-1
    if pos==0:
        return [(freq,num)] + sorting_line
    elif pos==len(sorting_line):
        return sorting_line + [(freq,num)]
    else:
        return sorting_line[:pos] + [(freq,num)] + sorting_line[pos:]

r,c,k = map(int, input().split())
r-=1
c-=1
arr=[list(map(int,input().split())) for _ in range(3)]
print(solution(arr))