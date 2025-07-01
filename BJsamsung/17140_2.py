def solution(arr):
    global r,c,k
    for time in range(101):
        if r<len(arr) and c<len(arr[0]):
            if arr[r][c]==k:
                return time
        arr = get_next_arr(arr)     # under O(100,000)

    return -1

def print_arr(arr):
    for line in arr:
        for ele in line:
            print(ele, end=' ')
        print()
    print()

def get_next_arr(arr):
    R = len(arr)
    C = len(arr[0])

    if R>=C:
        new_arr = [None]*R
        max_line_len = 0
        for r in range(R):  #O(100)
            counter = [0]*101
            for c in range(C):  #O(100)
                counter[arr[r][c]] += 1
            new_line = get_next_line(counter)   #O( ? )
            max_line_len = max(max_line_len, len(new_line))
            new_arr[r] = new_line[:100] + [0]*(100-len(new_line))
        for r in range(R):  #O(100)
            new_arr[r] = new_arr[r][:max_line_len]
    else:
        dig_new_arr = [None]*C
        max_line_len = 0
        for c in range(C):  #O(100)
            counter = [0]*101
            for r in range(R):  #O(100)
                counter[arr[r][c]] += 1
            dig_new_line = get_next_line(counter)   #O( ? )
            max_line_len = max(max_line_len, len(dig_new_line))
            dig_new_arr[c] = dig_new_line[:100] + [0]*(100-len(dig_new_line))
        new_arr = []
        for i, line_tuple in enumerate(zip(*dig_new_arr)):  #O(100)
            if i==max_line_len:
                break
            new_arr.append(list(line_tuple))
    return new_arr

"""
O(900) 이내로
"""
def get_next_line(counter):
    new_line = []
    for num in range(1,101):
        count = counter[num]
        if count==0:
            continue
        if len(new_line) == 0:
            new_line.append((count,num))
            continue
        new_line = binary_search(new_line, num, count)
    if len(new_line) == 0:
        raise Exception("sorting 에서 오류")
    final_line = []
    for ele in new_line:
        final_line.append(ele[1])
        final_line.append(ele[0])
    return final_line

def binary_search(line, num, count):
    st=0
    ed=len(line)-1
    pos=None
    for _ in range(len(line)+10):
        if st > ed:
            pos = max(st,ed)
            break
        mid = (st+ed)//2
        if line[mid][0] > count:
            ed = mid-1
        elif line[mid][0] < count:
            st = mid+1
        elif line[mid][0] == count:
            st = mid+1
            for _ in range(len(line)+10):
                if st > ed:
                    pos = max(st,ed)
                    break
                mid = (st+ed)//2
                if line[mid][0] > count:
                    ed = mid-1
                    continue
                elif line[mid][0] == count:
                    st = mid+1
                else:
                    raise Exception("오류 발생")

    if pos == len(line):
        return line + [(count,num)]
    elif pos == 0:
        return [(count,num)] + line
    else:
        return line[:pos] + [(count,num)] + line[pos:]


r,c,k = map(int,input().split())
r-=1
c-=1
arr=[]
for _ in range(3):
    arr.append(list(map(int,input().split())))

print(solution(arr))