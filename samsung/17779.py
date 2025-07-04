def solution():
    min_diff = float('inf')
    n=int(input())
    a1=[list(map(int,input().split())) for _ in range(n)]
    for x in range(n-2):
        for y in range(1,n-1):
            for d1 in range(1,n):
                if y-d1<0:
                    break
                for d2 in range(1,n):
                    if x+d1+d2>=n or y+d2>=n:
                        break
                    # make 선거구 map
                    a2 = [[1]*n for _ in range(n)]
                    for r in range(x+d2+1):
                        for c in range(y+1,n):
                            a2[r][c]=2
                    for r in range(x+d1,n):
                        for c in range(y-d1+d2):
                            a2[r][c]=3
                    for r in range(x+d2+1,n):
                        for c in range(y-d1+d2,n):
                            a2[r][c]=4

                    dist5_dict = {x:[y]}
                    for i1 in range(d1+1):
                        x1,y1 = x+i1, y-i1
                        if x1 not in dist5_dict:
                            dist5_dict[x1] = [y1]
                        else:
                            dist5_dict[x1].append(y1)
                        x4,y4 = x+d2+i1,y+d2-i1
                        if x4 not in dist5_dict:
                            dist5_dict[x4] = [y4]
                        else:
                            dist5_dict[x4].append(y4)
                    for i2 in range(d2+1):
                        x2, y2 = x + i2, y + i2
                        if x2 not in dist5_dict:
                            dist5_dict[x2] = [y2]
                        else:
                            dist5_dict[x2].append(y2)
                        x3,y3 = x+d1+i2, y-d1+i2
                        if x3 not in dist5_dict:
                            dist5_dict[x3] = [y3]
                        else:
                            dist5_dict[x3].append(y3)
                    for tx in dist5_dict.keys():
                        ty_li=dist5_dict[tx]
                        if len(ty_li)==1:
                            a2[tx][ty_li[0]]=5
                        else:
                            y1,y2 = min(ty_li),max(ty_li)
                            a2[tx][y1:y2+1] = [5]*(y2-y1+1)
                    # pm(a2)
                    populations=[0]*5
                    for r in range(n):
                        for c in range(n):
                            populations[a2[r][c]-1] += a1[r][c]
                    min_diff = min(min_diff, max(populations)-min(populations))
    print(min_diff)
solution()      # 240ms

def solution2():
    min_diff = float('inf')
    n=int(input())
    a1=[list(map(int,input().split())) for _ in range(n)]
    for x in range(n-2):
        for y in range(1,n-1):
            for d1 in range(1,n):
                if y-d1<0:
                    break
                for d2 in range(1,n):
                    if x+d1+d2>=n or y+d2>=n:
                        break
                    count=[0]*5
                    for r in range(n):
                        for c in range(n):
                            if r<x+d1 and c<=y:
                                if r>=x and c>=y-(r-x):
                                    count[5-1] += a1[r][c]
                                    continue
                                count[1-1] += a1[r][c]
                                continue
                            if r>=x+d1 and c<y-d1+d2:
                                if r<=x+d1+d2 and c>=y-d1+(r-x-d1):
                                    count[5-1] += a1[r][c]
                                    continue
                                count[3-1] += a1[r][c]
                                continue
                            if r<=x+d2 and c>y:
                                if r>=x+1 and c<=y+(r-x):
                                    count[5-1] += a1[r][c]
                                    continue
                                count[2-1] += a1[r][c]
                                continue
                            if r>x+d2 and c>=y-d1+d2:
                                if c<=y+d2-(r-(x+d2)) and r<=x+d2+d1:
                                    count[5-1] += a1[r][c]
                                    continue
                                count[4-1] += a1[r][c]
                                continue
                            count[5 - 1] += a1[r][c]
                            continue
                    min_diff=min(min_diff, max(count)-min(count))
    print(min_diff)
solution2()     # 312ms