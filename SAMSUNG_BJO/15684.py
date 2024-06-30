def solution(arr):
    global N, M, H
    if test(arr):
        return 0
    return add_3_test(arr)

def test(arr):
    global N, M, H
    for cur_col in range(N):
        original_cur_col = cur_col
        for row_idx in range(H):
            if arr[row_idx][cur_col] == 1:
                cur_col += 1
            elif cur_col > 0:
                if arr[row_idx][cur_col-1] == 1:
                    cur_col -= 1
        if original_cur_col != cur_col:
            return False
    return True

def add_3_test(arr):
    global N, M, H
    min_answer=4
    for num1 in range(N*H):
        r1,c1 = num1//N, num1 % N
        if arr[r1][c1] == 1 or c1 == N-1:
            continue
        elif arr[r1][c1] == 0:
            if arr[r1][c1 + 1] == 1 or (c1 != 0 and arr[r1][c1 - 1] == 1):  # 양옆에 있음X
                continue
            arr[r1][c1] = 1
            if test(arr):
                return 1

            for num2 in range(num1+1, N*H):
                r2, c2 = num2 // N, num2 % N
                if arr[r2][c2] == 1 or c2 == N - 1:
                    continue
                elif arr[r2][c2] == 0:
                    if arr[r2][c2 + 1] == 1 or (c2 != 0 and arr[r2][c2 - 1] == 1):  # 양옆에 있음X
                        continue
                    arr[r2][c2] = 1
                    if test(arr):
                        min_answer=min(min_answer,2)

                    for num3 in range(num2+1, N*H):
                        r3, c3 = num3 // N, num3 % N
                        if arr[r3][c3] == 1 or c3 == N - 1:
                            continue
                        elif arr[r3][c3] == 0:
                            if arr[r3][c3 + 1] == 1 or (c3 != 0 and arr[r3][c3 - 1] == 1):  # 양옆에 있음X
                                continue
                            arr[r3][c3] = 1
                            if test(arr):
                                min_answer=min(min_answer,3)

                            arr[r3][c3] = 0
                    arr[r2][c2] = 0
            arr[r1][c1] = 0

    if min_answer==4:
        return -1
    else:
        return min_answer


# import time
N,M,H = map(int,input().split())
arr = [[0]*N for _ in range(H)]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1

# st=time.time()
print(solution(arr))
# print(f"took {time.time() - st}")