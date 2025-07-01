from collections import deque
def solution():

    # INPUTS
    L, N, Q = map(int, input().split())
    # map
    A = []
    for _ in range(L):
        line = list(map(int, input().split()))
        A.append(line)
    # loc
    knights = {}
    for ki in range(N):
        r, c, h, w, k = map(int, input().split())
        r -= 1; c -= 1; ki+=1
        knights[ki] = ((r, c, h, w, k, 0))

    order = []
    for _ in range(Q):
        ki, d = map(int, input().split())
        order.append((ki, d))

    # print("일단 함정/벽 지도")
    # p(A)


    for ki, di in order:
        # print(f"______{ki}에 대한 명령______")
        if knights[ki][4]<=0:   #명령 받은애 죽어있어.
            # print("명령 받은애가 죽어있네")
            continue

        # print("수행 전 기사 지도")
        # p(knights, L)
        # print("변하기 전 - ",knights)
        new_knights = update(A,knights,ki,di)
        if new_knights!=None:
            # print("변한 기사들 - ",new_knights)
            knights = new_knights

            # print("수행 후 기사 지도")
            # p(knights, L)
        # else:
        #     print("안 변했다이")

    answer = 0
    for ki in knights.keys():
        _,_,_,_,k,d = knights[ki]
        if k>0:
            answer += d

    return answer



# 업데이트된 B랑, knights, 총 damge 반환.
def update(A, knights, ki, di):

    knights = knights.copy()
    L = len(A)
    diff = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 0상 1우 2하 3좌
    K = [[0]*L for _ in range(L)]
    for tmp_ki in knights.keys():
        r,c,h,w,health,damge = knights[tmp_ki]
        if health<=0:
            continue
        for kr in range(r,r+h):
            for kc in range(c,c+w):
                if K[kr][kc]>0:
                    raise Exception(f"{tmp_ki}넣으려 한 {kr,kc}에 {K[kr][kc]}가 있네")
                K[kr][kc] = tmp_ki

    # knights를 업데이트한다 - BFS
    _, _, _, _, backup_k, backup_d = knights[ki]
    dq = deque([ki])
    nxt_dq = set()
    while dq:
        curki = dq.pop()
        cr, cc, ch, cw, ck, cd = knights[curki]
        dr, dc = diff[di]

        for nr in range(cr+dr,cr+dr+ch):
            for nc in range(cc+dc,cc+dc+cw):

                if not (0<=nr<L and 0<=nc<L) or A[nr][nc]==2:
                    return None

                if A[nr][nc]==1:
                    ck -= 1
                    cd += 1

                if K[nr][nc] != curki and K[nr][nc]>0 and K[nr][nc] not in nxt_dq:
                    nxt_dq.add(K[nr][nc])

        knights[curki] = (cr+dr, cc+dc, ch, cw, ck, cd)
        dq = nxt_dq

    r,c,h,w,_,_ = knights[ki]
    knights[ki] = (r,c,h,w,backup_k, backup_d)
    return knights

    # 새로 B 만든다.

def p(knights,L):

    K = [[0]*L for _ in range(L)]
    for ki in knights.keys():
        r,c,h,w,k,d = knights[ki]
        if k<=0:
            continue
        for nr in range(r,r+h):
            for nc in range(c,c+w):
                K[nr][nc] = ki

    for l in K:
        for e in l:
            print(e, end=' ')
        print()
    print()

# A = [[0, 0, 1, 0], [0, 0, 1, 0], [1, 1, 0, 1], [0, 0, 2, 0]]
# knights = {1: (0, 1, 2, 1, 5, 0), 2: (1, 0, 2, 1, 1, 0), 3: (2, 1, 1, 2, 3, 0)}
# orders = [(1, 2), (2, 1), (3, 3)]
print(solution())