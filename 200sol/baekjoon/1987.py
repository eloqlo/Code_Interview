R,C = map(int, input().split())
A = []
for _ in range(R):
    A.append(list(input()))
diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_val = 0
stack = set(A[0][0])

def dfs(r, c, depth):
    global R,C,A,diff,max_val,stack

    for dr,dc in diff:
        nr,nc = r+dr, c+dc
        if 0<=nr<R and 0<=nc<C:
            if A[nr][nc] not in stack:
                stack.add(A[nr][nc])
                dfs(nr, nc,depth+1)
                stack.remove(A[nr][nc])

    max_val = max(max_val, depth)

dfs(0,0,1)
print(max_val)

