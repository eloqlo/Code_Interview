def _copy_arr(arr):
    new_arr = []
    for line in arr:
        new_arr.append(line.copy())
    return new_arr

def _spread_lab(lab, virus_location):
    N,M = len(lab), len(lab[0])
    cur = [loc.copy() for loc in virus_location]
    visit = [[0]*M for _ in range(N)]

    dr = [0,0,1,-1]
    dc = [-1,1,0,0]
    while cur:
        nxt = []
        for r,c in cur:
            for di in range(4):
                nr,nc = r+dr[di], c+dc[di]
                if 0<=nr<N and 0<=nc<M and lab[nr][nc]==0 and visit[nr][nc]==0:
                    visit[nr][nc] = 1       # Visit Check
                    nxt.append([nr,nc])
                    lab[nr][nc] = 2         # VIRUS Check
        cur = nxt
    return


def solution():
    N,M = map(int, input().split())
    arr = []
    virus_location = []
    for r in range(N):
        new_line = []
        for c, element in enumerate(map(int, input().split())):
            new_line.append(element)
            if element==2:
                virus_location.append([r,c])
        arr.append(new_line)

    # Brute-force + BFS
    # O(N^3 * M^3) == O(270,000)
    MAX_AREA = 0
    for w1 in range(N*M):
        wr1, wc1 = w1//M, w1%M
        if arr[wr1][wc1]!=0:
            continue
        for w2 in range(w1+1,N*M):
            wr2, wc2 = w2//M, w2%M
            if arr[wr2][wc2]!=0:
                continue
            for w3 in range(w2+1,N*M):
                wr3, wc3 = w3//M, w3%M
                if arr[wr3][wc3]!=0:
                    continue
                lab = _copy_arr(arr)
                lab[wr1][wc1] = 1
                lab[wr2][wc2] = 1
                lab[wr3][wc3] = 1
                
                _spread_lab(lab, virus_location)

                counter = 0
                for line in lab:
                    for element in line:
                        if element == 0:
                            counter += 1
                MAX_AREA = max(MAX_AREA, counter)
    
    return MAX_AREA



if __name__=="__main__":
    result = solution()
    print(result)