def print_arr(arr):
    for line in arr:
        for ele in line:
            print(ele, end='')
        print()
    print('-----')

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
        arr = transform(arr)

def transform(arr):
    if len(arr)>= len(arr[0]):
        return get_new_arr_rowwise(arr)
    else:
        arr = list(zip(*arr))
        arr = get_new_arr_rowwise(arr)
        return list(zip(*arr))

def get_new_arr_rowwise(arr):
    maxlen = 0
    new_arr=[]
    for line in arr:
        counter= {}

        for num in line:
            if num == 0:
                continue
            if num not in counter:
                counter[num]=1
            else:
                counter[num]+=1

        tmp_line = sorted(counter.items(), key=lambda x:(x[1],x[0]))
        new_line = []
        for freq,num in tmp_line:
            new_line.append(freq)
            new_line.append(num)

        maxlen = min(max(maxlen,len(new_line)),100)
        new_arr.append(new_line[:maxlen])

    new_arr = [new_line+[0]*(maxlen-len(new_line)) for new_line in new_arr]
    return new_arr

r,c,k = map(int,input().split())
r-=1; c-=1
arr=[list(map(int,input().split())) for _ in range(3)]
solution(arr)