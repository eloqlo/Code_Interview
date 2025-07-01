def p(A):
    print()
    for l in A:
        for e in l:
            if e==-1:
                print('R', end='\t')
            elif e>0:
                print(e, end='\t')
            else:
                print('.', end='\t')
        print()

def solution():

    N,M,P,C,D = map(int, input().split())
    A = [[0]*N for _ in range(N)]
    rr,rc = map(int, input().split())
    rr-=1; rc-=1
    A[rr][rc] = -1  # 루돌프
    san_loc_dict = {}
    for _ in range(P):
        si, sr, sc = map(int, input().split())
        sr-=1; sc-=1
        san_loc_dict[si] = (sr, sc)
        A[sr][sc] = si  # 산타
    diff_san = [(-1,0), (0,1), (1,0), (0,-1)]
    diff_rud = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
    SCORE = [0]*(P+1)   # idx가 산타 번호 (1~P)
    cur_stun_san = set()
    prev_stun_san = set()


    for turn_idx in range(M):

        # print(f"_____________{turn_idx+1} TURN START _____________")

        #1 루돌프랑 가까운 산타 찾기
        near_sr, near_sc, min_dist = -1, -1, 1e6
        san_loc = list(san_loc_dict.values())
        san_loc.sort(key=lambda x:(-x[0],-x[1]))
        for tmp_sr, tmp_sc in san_loc:
            dist = (rr - tmp_sr)**2 + (rc - tmp_sc)**2
            if dist < min_dist:
                min_dist = dist
                near_sr = tmp_sr
                near_sc = tmp_sc
        """
        near_sr, near_sc : 가까이 산타 위치
        """

        #2 그 산타랑 가장 가까워지는 주위 1칸
        rud_nr, rud_nc, min_dist = None, None, 1e6
        rud_dr, rud_dc = None,None
        for dr, dc in diff_rud:
            nrr, nrc = rr + dr, rc + dc
            if not (0<=nrr<N and 0<=nrc<N):
                continue
            dist = (nrr - near_sr)**2 + (nrc - near_sc)**2
            if dist < min_dist:
                min_dist = dist
                rud_nr, rud_nc = nrr, nrc
                rud_dr, rud_dc = dr, dc
        """
        rud_rr, rud_rc : 새로운 루돌프 위치
        rud_dr, rud_dc : 새로운 루돌프 방향
        """

        # p(A)
        # print(f"NOW R MOVE")

        #3 루돌프 이동 (빈칸, 산타)
        if A[rud_nr][rud_nc] == 0:
            A[rr][rc] = 0
            A[rud_nr][rud_nc] = -1
            rr, rc = rud_nr, rud_nc
        elif A[rud_nr][rud_nc] > 0:
            A[rr][rc] = 0
            rr, rc = rud_nr, rud_nc
            hit_si = A[rr][rc]              # 맞은 산타 번호
            SCORE[hit_si] += C          #1 산타 점수 획득
            A[rr][rc] = -1              # 루돌프 맵 업데이트

            #3 산타 밀림
            # print(f"{hit_si} GOT HIT + STUNED + {C}만큼 빠이")
            nsr, nsc = rr + rud_dr*C, rc + rud_dc*C
            if not (0<=nsr<N and 0<=nsc<N):
                san_loc_dict.pop(hit_si)   # 경외착지, 산타 사망
            elif A[nsr][nsc]==0:
                cur_stun_san.add(hit_si)
                A[nsr][nsc] = hit_si
                san_loc_dict[hit_si] = (nsr,nsc)
            elif A[nsr][nsc]>0:
                cur_stun_san.add(hit_si)
                while True:
                    tmp_si = A[nsr][nsc]
                    A[nsr][nsc] = hit_si
                    san_loc_dict[hit_si] = (nsr, nsc)

                    # TODO SANITY CHECK
                    # 산타 밀리는 CODE
                    nsr, nsc = nsr + rud_dr, nsc + rud_dc
                    hit_si = tmp_si
                    if tmp_si == 0:
                        break
                    if not (0 <= nsr < N and 0 <= nsc < N):
                        san_loc_dict.pop(hit_si)
                        break

        # p(A)
        # print("NOW S MOVE")
        """
        rr, rc : 루돌프 위치
        cur_stun_san : 부딪혀서 스턴된 산타들
        san_loc_dict : 산타 위치 dict
        diff_san : 상우하좌, 가까워지는 순서 우선순위
        """
        #4 산타의 이동
        for tmpsi in sorted(list(san_loc_dict.keys())):
            # 이동할 곳 찾기 (mr,mc),(mdr,mdc)
            if tmpsi not in san_loc_dict:
                continue
            if (tmpsi in cur_stun_san) or (tmpsi in prev_stun_san):
                continue
            tmpsr, tmpsc = san_loc_dict[tmpsi]
            cur_dist = (rr - tmpsr) ** 2 + (rc - tmpsc) ** 2
            min_dist = 1e6
            mr,mc = None,None
            mdr,mdc = None,None
            for dr,dc in diff_san:
                nr, nc = tmpsr + dr, tmpsc + dc
                if (0 <= nr < N and 0 <= nc < N) and A[nr][nc]<=0:
                    dist = (rr - nr) ** 2 + (rc - nc) ** 2
                    if dist < min_dist and dist < cur_dist:
                        min_dist = dist
                        mr, mc = nr, nc
                        mdr, mdc = dr, dc
            if mr == None:
                # 이동 불가능
                continue

            # 이동하기
            if A[mr][mc]==0:
                A[mr][mc] = tmpsi
                A[tmpsr][tmpsc] = 0
                san_loc_dict[tmpsi] = (mr,mc)
                continue
            else:
                """
                루돌프 충돌
                1. D만큼 점수
                2. 반대방향 D 밀리기
                3. 상호작용
                """
                A[tmpsr][tmpsc] = 0
                cur_stun_san.add(tmpsi)     # 기절
                SCORE[tmpsi] += D
                # print(f"{tmpsi} HIT RUD, {D}만큼 빠이")
                """
                hitr, hitc = tmpsi의 착지위치
                -mdr, -mdc = 튕겨난 방향
                """
                # TODO SANITY CHECK: 산타 이동 후 루돌프 충돌, 산타 연쇄작용
                hitr, hitc = mr - mdr*D, mc - mdc*D
                nxt_si = tmpsi
                while True:
                    if 0 <= hitr < N and 0 <= hitc < N:
                        tmp2si = A[hitr][hitc]
                        A[hitr][hitc] = nxt_si
                        san_loc_dict[nxt_si] = (hitr, hitc)

                        hitr, hitc = hitr - mdr, hitc - mdc
                        nxt_si = tmp2si
                        if nxt_si == 0:
                            break
                    else:
                        san_loc_dict.pop(nxt_si)
                        break


        # END OF TURN
        prev_stun_san = cur_stun_san
        cur_stun_san = set()
        for cur_si in san_loc_dict.keys():
            SCORE[cur_si]+=1

        # p(A)
        # print("FIN")
        # print(f"CURRENT SANTA DICTIONARY {san_loc_dict}")
        # print(f"CURRENT SANTA SCORE {SCORE[1:]}")
        # print(f"NEXT PREV STUNED SANTA ", prev_stun_san)


    return SCORE[1:]


ans = solution()
for e in ans:
    print(e, end=' ')