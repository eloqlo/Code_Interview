def end_check(A):
    ans = [1,2,3,4,5,6,7,8,0]
    for i in range(9):
        r = i//3
        c = i%3
        if A[r][c]!=ans[i]:
            return False
    return True

def solution():
    A = [list(map(int, input().split())) for _ in range(3)]
    for r in range(3):
        for c in range(3):
            if A[r][c]==0:
                zr,zc = r,c