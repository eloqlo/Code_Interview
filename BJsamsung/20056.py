def solution():
    N,M,K = map(int,input().split())
    board=[[[] for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        r,c,m,s,d = map(int,input().split())
        board[r-1][c-1].append((m,s,d))
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]

    for _ in range(K):
        new_board = [[[] for _ in range(N)] for _ in range(N)]
        more_than_two = set()
        for r in range(N):
            for c in range(N):
                foo = board[r][c]
                if len(foo)==0:
                    continue
                for m,s,d in foo:
                    nr, nc = r+dr[d]*s, c+dc[d]*s
                    nr, nc = (nr+N*251)%N, (nc+N*251)%N
                    new_board[nr][nc].append((m,s,d))
                    if len(new_board[nr][nc])>1:
                        more_than_two.add((nr,nc))

        for r,c in list(more_than_two):
            foo = list(zip(*new_board[r][c]))   # sanity check
            nm = sum(foo[0])//5
            ns = sum(foo[1])//len(new_board[r][c])
            if nm==0:
                new_board[r][c] = []
                continue        # 디버깅의 원흉..
            if odd_even(foo[2]):
                bar = [(nm,ns,nd*2) for nd in range(4)]
            else:
                bar = [(nm,ns,nd*2+1) for nd in range(4)]
            new_board[r][c] = bar
        board = new_board

    count = 0
    for r in range(N):
        for c in range(N):
            foo = board[r][c]
            if foo:
                count += sum([ele[0] for ele in board[r][c]])
    print(count)

def pm(a):
    for l in a:
        for e in l:
            print(e, end=' ')
        print()
    print('__________')

def odd_even(arr):
    return sum([ele%2 for ele in arr])==len(arr) or sum([ele%2 for ele in arr])==0

solution()