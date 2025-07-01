N = int(input())
arr = list(map(int,input().split()))
ops = list(map(int,input().split()))
max_val = -1e9
min_val = +1e9

def compute_min_max(num, idx):
    global arr, ops, max_val, min_val

    if sum(ops)==0:
        max_val = max(num, max_val)
        min_val = min(num, min_val)
        return

    # +, -, x, %
    if ops[0]>0:
        ops[0]-=1
        compute_min_max(num+arr[idx], idx+1)
        ops[0]+=1
    if ops[1]>0:
        ops[1]-=1
        compute_min_max(num-arr[idx], idx+1)
        ops[1]+=1
    if ops[2]>0:
        ops[2]-=1
        compute_min_max(num*arr[idx], idx+1)
        ops[2] += 1
    if ops[3] > 0:
        ops[3] -= 1
        ###########################################
        if num < 0:
            tmp = (-num)//arr[idx]
            compute_min_max(-tmp, idx+1)
        else:
            compute_min_max(num//arr[idx], idx+1)
        ###########################################
        # compute_min_max(int(num/arr[idx]), idx+1)
        # ops[3] += 1


compute_min_max(arr[0],1)
print(max_val, min_val, sep='\n')