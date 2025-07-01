
from collections import defaultdict
def p(A):
    print()
    for l in A:
        for e in l:
            print(e, end=' ')
        print()
def nxt_comb(cctv, cctv_di):
    """
    cctv        :
    cctv_di     :
    """
    # 다음 증가시킬 곳 찾기
    for cctv_idx in range(len(cctv_di)-1, -1, -1):
        cur_type = cctv[cctv_idx][0]
        cur_di = cctv_di[cctv_idx]
        if _max_di(cur_type, cur_di):
            if cctv_idx==0:
                return None
            cctv_di[cctv_idx]=0
            continue
        else:
            cctv_di[cctv_idx] += 1
            return cctv_di
def _max_di(type, di):
    if type==2:
        if di==1:
            return True
        return False
    else:
        if di==3:
            return True
        return False

def solution():
    # CONFIGS
    N,M = map(int, input().split())
    A=[]
    cctv = []
    cctv_5=[]
    SIZE = N*M
    for r in range(N):
        line = list(map(int, input().split()))
        A.append(line)
        for c, ele in enumerate(line):
            if 1<=ele<=5:
                if ele==5:
                    cctv_5.append((r,c))
                else:
                    cctv.append([ele,r,c])    # 번호, r, c, 방향
                SIZE -= 1
            elif ele == 6:
                SIZE -= 1
    diff = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북동남서

    # INITAL SETTING
    for r, c in cctv_5:
        # 위치별로 사방으로 계산
        for dr, dc in diff:
            for foo in range(1,max(N,M)):
                nr, nc = r + dr*foo, c + dc*foo
                if 0<=nr<N and 0<=nc<M:
                    if A[nr][nc] == 6:
                        break
                    if A[nr][nc] == 0:
                        A[nr][nc] = "#"
                        SIZE -= 1
                    elif A[nr][nc] == "#":
                        continue


    # CALC COMBINATION
    cctv_di = [0]*len(cctv)
    MIN_SIZE = SIZE



    """
    loop 
        make di combination
        copy map
        set map + calc size
        min(MIN_SIZE, CUR_SIZE)
    """
    while True:
        if cctv_di == None:
            break

        CUR_SIZE = SIZE
        A_new = [line.copy() for line in A]
        for (curtype, cr, cc), curdi in zip(cctv, cctv_di):
            # print(f"type {curtype}/ cr,cr {cr,cc}/ di {curdi}")
            if curtype==1:
                dr,dc = diff[curdi]
                for co in range(1,max(N,M)):
                    nr = cr + dr*co
                    nc = cc + dc*co
                    if 0<=nr<N and 0<=nc<M:
                        if A_new[nr][nc] == 6:
                            break
                        elif A_new[nr][nc] == 0:
                            A_new[nr][nc] = '#'
                            CUR_SIZE -= 1
                    else:
                        break
            elif curtype==2:
                if curdi==0:
                    #TODO 가로
                    tmp_diff = [(-1,0),(1,0)]
                    for dr, dc in tmp_diff:
                        for co in range(1, max(N, M)):
                            nr = cr + dr * co
                            nc = cc + dc * co
                            if 0 <= nr < N and 0 <= nc < M:
                                if A_new[nr][nc] == 6:
                                    break
                                elif A_new[nr][nc] == 0:
                                    A_new[nr][nc] = '#'
                                    CUR_SIZE -= 1
                            else:
                                break
                else:
                    tmp_diff = [(0,-1), (0,1)]
                    for dr, dc in tmp_diff:
                        for co in range(1, max(N, M)):
                            nr = cr + dr * co
                            nc = cc + dc * co
                            if 0 <= nr < N and 0 <= nc < M:
                                if A_new[nr][nc] == 6:
                                    break
                                elif A_new[nr][nc] == 0:
                                    A_new[nr][nc] = '#'
                                    CUR_SIZE -= 1
                            else:
                                break
            elif curtype==3:
                newdi = (curdi+1)%4
                for dr, dc in [diff[curdi], diff[newdi]]:
                    for co in range(1, max(N, M)):
                        nr = cr + dr * co
                        nc = cc + dc * co
                        if 0 <= nr < N and 0 <= nc < M:
                            if A_new[nr][nc] == 6:
                                break
                            elif A_new[nr][nc] == 0:
                                A_new[nr][nc] = '#'
                                CUR_SIZE -= 1
                        else:
                            break
            elif curtype==4:
                tmp_diff = diff.copy()
                tmp_diff.pop(curdi)
                for dr,dc in tmp_diff:
                    for co in range(1, max(N, M)):
                        nr = cr + dr * co
                        nc = cc + dc * co
                        if 0 <= nr < N and 0 <= nc < M:
                            if A_new[nr][nc] == 6:
                                break
                            elif A_new[nr][nc] == 0:
                                A_new[nr][nc] = '#'
                                CUR_SIZE -= 1
                        else:
                            break
        # 모든 경우의 수 적용 끝
        MIN_SIZE = min(MIN_SIZE, CUR_SIZE)
        cctv_di = nxt_comb(cctv, cctv_di)   # 다음 경우의 수
        #while_glue
    #glue
    return MIN_SIZE


print(solution())