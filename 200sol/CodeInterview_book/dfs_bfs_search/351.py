def solution(arr, t_arr):

    N = len(arr)
    count=0
    for w1 in range(N**2):
        for w2 in range(w1+1,N**2):
            for w3 in range(w2+1,N**2):
                count+=1
                r1, c1 = w1 // N, w1 % N
                r2, c2 = w2 // N, w2 % N
                r3, c3 = w3 // N, w3 % N
                arr_copy = [line.copy() for line in arr]
                if arr_copy[r1][c1]!="X" or arr_copy[r2][c2]!="X" or arr_copy[r3][c3]!="X":
                    continue
                else:
                    arr_copy[r1][c1] = arr_copy[r2][c2] = arr_copy[r3][c3] = "O"
                if not get_caught(arr_copy, t_arr, count):
                    return "YES"

    return "NO"

def get_caught(arr, t_arr, count):
    # print_map(arr, count)
    arr_copy = [line.copy() for line in arr]
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    for di in range(4):
        for r,c in t_arr:
            for i in range(1,len(arr)):
                nr = r + dr[di]*i
                nc = c + dc[di]*i
                if 0<=nr<len(arr) and 0<=nc<len(arr):
                    if arr[nr][nc] == "O":
                        break
                    elif arr[nr][nc] == "S":
                        return True
                    else:
                        arr_copy[nr][nc] = "*"
                        continue
                else:
                    break

    return False

def print_map(arr,count):
    print(f"---- at {count} ----")
    for line in arr:
        for ele in line:
            print(ele, end=' ')
        print()

N = int(input())
arr = []
t_arr=[]
s_arr=[]
for r in range(N):
    line=[]
    for c, ele in enumerate(input().split()):
        if ele == "S":
            s_arr.append((r,c))
        elif ele == "T":
            t_arr.append((r,c))
        line.append(ele)
    arr.append(line)

# 모든 경우의 수에 대해 판단 ㄱㄱ
ans = solution(arr,t_arr)
print(ans)