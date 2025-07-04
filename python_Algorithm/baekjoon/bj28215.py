def solution():

    # INPUTS
    N, K = map(int,input().split())
    houses = []
    for _ in range(N):
        r,c = map(int,input().split())
        houses.append((r,c))


    pg = pointer_gen(N,K)
    ANSWER = float('inf')
    for pl in pg:
        cur_dist = [float('inf')]*N
        for hi in range(N):
            for pnt in pl:
                if pnt==hi:
                    cur_dist[hi] = 0
                    continue
                dist = calc_dist(houses, hi, pnt)
                cur_dist[hi] = min(cur_dist[hi], dist)
        ANSWER = min(ANSWER, max(cur_dist))
    return ANSWER


def calc_dist(houses,hi,pnt):
    hr,hc = houses[hi]
    dr,dc = houses[pnt]
    return abs(hr-dr) + abs(hc-dc)


def pointer_gen(N,K):
    if K==1:
        for p1 in range(N):
            yield [p1]
    elif K==2:
        for p1 in range(N-1):
            for p2 in range(p1+1,N):
                yield [p1,p2]
    elif K==3:
        for p1 in range(N-2):
            for p2 in range(p1+1,N-1):
                for p3 in range(p2+1,N):
                    yield [p1,p2,p3]
    else:
        raise Exception()


print(solution())