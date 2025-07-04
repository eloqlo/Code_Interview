def solution(N,M,H,arr):
    def test(arr):
        for cur_col in range(N):
            # checking for each column
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

    def add_1_test(arr):
        for num in range(N*H):
            r = num//N
            c = num%N
            if arr[r][c]==1 or c==N-1:
                continue
            else:
                tmp_arr = [line.copy() for line in arr]
                tmp_arr[r][c] = 1
                if test(tmp_arr):
                    return True
        return False

    def add_2_test(arr):
        for num1 in range(N*H):
            r1,c1 = num1//N, num1%N
            if arr[r1][c1] == 1 or c1==N-1:
                continue
            for num2 in range(num1+1, N*H):
                r2,c2 = num2//N, num2%N
                if arr[r2][c2] == 1 or c2==N-1:
                    continue
                else:
                    tmp_arr = [line.copy() for line in arr]
                    tmp_arr[r1][c1] = 1
                    tmp_arr[r2][c2] = 1
                    if test(tmp_arr):
                        return True
        return False

    def add_3_test(arr):
        for num1 in range(N*H):
            r1,c1 = num1//N, num1%N
            if arr[r1][c1] == 1 or c1==N-1:
                continue
            for num2 in range(num1+1, N*H):
                r2,c2 = num2//N, num2%N
                if arr[r2][c2] == 1 or c2==N-1:
                    continue
                for num3 in range(num2+1, N * H):
                    r3,c3 = num3 // N, num3 % N
                    if arr[r3][c3] == 1 or c3==N-1:
                        continue
                    else:
                        tmp_arr = [line.copy() for line in arr]
                        tmp_arr[r1][c1] = 1
                        tmp_arr[r2][c2] = 1
                        tmp_arr[r3][c3] = 1
                        if test(tmp_arr):
                            return True
        return False


    if test(arr):
        return 0
    if add_1_test(arr):
        return 1
    if add_2_test(arr):
        return 2
    if add_3_test(arr):
        return 3
    return -1




N,M,H = map(int, input().split())
arr = [[0]*N for _ in range(H)]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1

print(solution(N,M,H, arr))