def battle(p1, p2, players):
    _, _, p1d, p1s, p1g = players[p1]
    _, _, p2d, p2s, p2g = players[p2]

    if p1s + p1g > p2s + p2g:
        winner = p1
        loser = p2
    elif p1s + p1g == p2s + p2g:
        if p1s > p2s:
            winner = p1
            loser = p2
        else:
            winner = p2
            loser = p1
    else:
        winner = p2
        loser = p1

    score = abs((p1s+p1g) - (p2s+p2g))
    return winner, loser, score

def gun_swap(G,r,c,players,pi):
    pg = players[pi][4]
    mi, mg = -1, pg
    for idx, gun in enumerate(G[r][c]):
        if gun > mg:
            mi = idx
            mg = gun
    if mi != -1:
        tmp = pg
        pg = G[r][c][mi]
        if tmp!=0:
            G[r][c] = G[r][c][:mi] + [tmp] + G[r][c][mi+1:]
        else:
            G[r][c].pop(mi)
    players[pi][4] = pg
    return G, players


def solution():

    # INPUTS
    N,M,K = map(int,input().split())
    G = []
    for r in range(N):
        G.append([])
        for ele in map(int,input().split()):
            G[r].append([ele])
    players = [None]
    P = [[0]*N for _ in range(N)]
    for pi in range(1,M+1):
        x,y,d,s = map(int,input().split())
        x-=1; y-=1
        players.append([x,y,d,s,0])
        P[x][y] = pi
    diff = [(-1,0),(0,1),(1,0),(0,-1)]
    SCORE = [0]*(M+1)


    # 라운드 진행
    for round in range(K):
        # print("________round ",round)
        for pi in range(1,M+1):

            pr, pc, pd, p_stat, p_gun = players[pi]

            # 플레이어 이동, 위치수정
            nr, nc = pr + diff[pd][0], pc + diff[pd][1]
            P[pr][pc] = 0
            if not (0 <= nr < N and 0 <= nc < N):
                pd = (pd + 2)%4
                players[pi][2] = pd
                nr, nc = pr + diff[pd][0], pc + diff[pd][1]
            players[pi][0], players[pi][1] = nr, nc

            # print(f"{pi} mv {pr,pc} -> {nr,nc}")

            # 결투 없다!
            if P[nr][nc] == 0:
                G, players = gun_swap(G, nr, nc, players, pi)
                P[nr][nc] = pi

                # print(f"{pi}가 이동한 곳에 아무도 없네")
                # print([players[i][-1] for i in range(1,len(players))])
                # print(SCORE[1:])
                # p(P,G)
                continue

            challengeri = P[nr][nc]
            winner, loser, score = battle(pi, challengeri, players)
            SCORE[winner] += score
            P[nr][nc] = winner

            # print(f"W{winner}, L{loser}, SCORE{SCORE[1:]}")
            # input()

            # loser gun 내려놓고
            _,_,ld,_,lg = players[loser]
            if lg>0:
                G[nr][nc].append(lg)
                players[loser][-1], lg = 0, 0

            # loser 이동
            for di in range(ld, ld+4):
                di = di%4
                lnr, lnc = nr + diff[di][0], nc + diff[di][1]
                if not (0<=lnr<N and 0<=lnc<N) or P[lnr][lnc]:
                    continue
                if P[lnr][lnc]==0:
                    break
            P[lnr][lnc] = loser
            players[loser][0] = lnr
            players[loser][1] = lnc
            players[loser][2] = di
            G,players = gun_swap(G,lnr,lnc,players,loser)

            #2 이긴 플레이어
            G,players = gun_swap(G,nr,nc,players,winner)

            # print("FIN FIN FIN")
            # print([players[i][-1] for i in range(1, len(players))])
            # print(SCORE[1:])
            # p(P,G)
            # one player fin
        # all players fin
    # round fin

    for ele in SCORE[1:]:
        print(ele, end=' ')


def p(P,G):

    print("___CURRENT POSITION___")
    for r in range(len(P)):
        for c in range(len(P)):

            if G[r][c]!=[0]:
                print(f"{G[r][c]}", end='')
            else:
                print(".",end='')

            if P[r][c]>0:
                print(f" {P[r][c]}", end='')

            print("\t",end='')
        print()
    print()
    input()


solution()

# answers=[]
# for test in range(3):
#     answers.append(solution())
# for ans in answers:
#     for ele in ans[1:]:
#         print(ele,end=' ')
#     print()