def solution():
    global arr, r,c,k
    if r >= len(arr) or c >= len(arr[0]):
        pass
    else:
        if arr[r][c]==k:
            return 0
    for it in range(1,101): # O(100)
        arr = change(arr)   # Less than 100,000
        if r>=len(arr) or c>=len(arr[0]):
            continue
        if arr[r][c]==k:
            return it
    return -1

def change(arr):
    is_col_wise = False
    if len(arr) < len(arr[0]):
        new_arr = [[0]*len(arr) for _ in range(len(arr[0]))]
        is_col_wise = True
        for r in range(len(arr)):
            for c in range(len(arr[0])):
                new_arr[c][r] = arr[r][c]
    else:
        new_arr = [line.copy() for line in arr]
        # 줄 별로 정렬 실행
    max_line_len = 0
    for line_idx, line in enumerate(new_arr):
        counter = [0]*101
        for ele in line:
            if ele > 0:
                counter[ele] += 1
            else:
                continue
        new_line = []
        for num in range(101):
            freq = counter[num]
            if freq == 0:
                continue
            if len(new_line) == 0:
                new_line.append((num, freq))
                continue
            new_line = _binary_search(new_line, num, freq)      # TODO 여기 문제 원흉
        new_arr[line_idx] = new_line
        max_line_len = max(max_line_len, len(new_line))

    # Zero-padding, crop it under 100 -- O(150)
    max_len = min(max_line_len*2, 100)
    for line_idx, line in enumerate(new_arr):
        new_line = []
        for ele_idx, ele in enumerate(line):
            if ele_idx==max_len:
                break
            new_line = new_line + [ele[0], ele[1]]
        new_arr[line_idx] = new_line + [0]*(max_len-len(new_line))

    # 다시 뒤집기
    if is_col_wise:
        tmp_arr = [[0]*len(new_arr) for _ in range(len(new_arr[0]))]
        for r in range(len(new_arr)):
            for c in range(len(new_arr[0])):
                tmp_arr[c][r] = new_arr[r][c]
        new_arr = tmp_arr
    return new_arr

def _binary_search(line, num, freq):   # O(400-600)
    """
    mid 에 새로운 원소가 와야함.
    """
    st = 0
    ed = len(line)-1
    for _ in range(100):
        mid = (st+ed)//2
        if st > ed:
            mid = max(st,ed)
            break
        if line[mid][1] == freq:
            st = mid
            for _ in range(100):
                prev_mid = mid
                mid = (st+ed)//2
                if prev_mid == mid:
                    break
                tmp_freq = line[mid][1]
                if tmp_freq > freq:
                    ed = mid-1
                    continue
                elif tmp_freq <= freq:
                    st = mid
                    continue
                else:
                    raise Exception("Error in _binary_search()")
            for mid in range(mid+1, len(line)+1):
                if mid == len(line):
                    break
                if line[mid][1] == freq:
                    if mid == len(line):
                        mid += 1
                    continue
                elif line[mid][1] != freq:
                    break
                else:
                    raise Exception("Error in _binary_search()")
            break
        elif line[mid][1] < freq:
            st = mid+1
        elif line[mid][1] > freq:
            ed = mid-1
        else:
            raise Exception("Error")

    if mid==len(line):
        return line + [(num, freq)]
    else:
        return line[:mid] + [(num, freq)] + line[mid:]

def print_arr(arr):
    for line in arr:
        for ele in line:
            print(ele, end=' ')
        print()

r,c,k = map(int, input().split())
r-=1
c-=1
arr = []
for _ in range(3):
    arr.append(list(map(int,input().split())))

print(solution())