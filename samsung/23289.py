from collections import deque

def p(A):
    for l in A:
        for e in l:
            print(e,end=' ')
        print()
    print()
def solution():
    # TODO sanity check
    def is_wall_btw(r1,c1,r2,c2):
        if r1-r2==0:
            if c1>c2:
                tr1,tr2 = r1,c1
                r1,c1 = r2,c2
                r2,c2 = tr1,tr2
            if (r1,c1,1) in W:
                return True
            return False
        else:
            if r1<r2:
                tr1, tr2 = r1, c1
                r1, c1 = r2, c2
                r2, c2 = tr1, tr2
            if (r1,c1,0) in W:
                return True
            return False
    def make_variation(inp,minus):
        return (inp==0)*minus

    R,C,K=map(int,input().split())
    A=[[0]*C for _ in range(R)]     # heat map
    B=[]    # warmer
    Z=[]    # check K
    drw=[0,0,-1,1]  # 오 왼 위 아래
    dcw=[1,-1,0,0]
    for r in range(R):
        for c, ele in enumerate(list(map(int,input().split()))):
            if 1<=ele<=4:
                B.append((r,c,ele-1))
            elif ele==5:
                Z.append((r,c))

    num_wall = int(input())
    W = set()    # walls
    for _ in range(num_wall):
        x, y, t = map(int,input().split())
        W.add((x-1,y-1,t))

    for time_counter in range(1,100+1):
        #1 WIND
        for wr,wc,wdi in B:
            cur_dr, cur_dc = drw[wdi], dcw[wdi]
            prev_loc = [(wr+cur_dr, wc+cur_dc)]
            visit = set()
            A[wr+cur_dr][wc+cur_dc] += 5    # FIRST HEAT
            for heat in range(4,0,-1):
                for prev_r, prev_c in prev_loc:
                    # make variations
                    # TODO 중복조회 제거해서 시간복잡도 개선 가능.
                    tmp_loc=[(prev_r,prev_c)]
                    for minus in [1,-1]:
                        tmp_r = prev_r + make_variation(cur_dr,minus)
                        tmp_c = prev_c + make_variation(cur_dc,minus)
                        if 0<=tmp_r<R and 0<=tmp_c<C:
                            if not is_wall_btw(tmp_r, tmp_c, prev_r, prev_c):
                                tmp_loc.append((tmp_r,tmp_c))
                    for tmp_r, tmp_c in tmp_loc:
                        # go stright
                        new_r, new_c = tmp_r+cur_dr, tmp_c+cur_dc
                        if 0 <= new_r < R and 0 <= new_c < C:
                            if not is_wall_btw(tmp_r,tmp_c,new_r,new_c):
                                if (new_r,new_c) not in visit:
                                    visit.add((new_r,new_c))
                                    A[new_r][new_c] += heat
                    #glue
                #glue
                prev_loc = list(visit)

        #2 Temperature adjustment
        A_anchor = [l.copy() for l in A]
        for r in range(R):
            for c in range(C):
                for tmp_di in range(4):
                    nr, nc = r+drw[tmp_di], c+dcw[tmp_di]
                    if 0<=nr<R and 0<=nc<C:
                        if A_anchor[nr][nc] < A_anchor[r][c]\
                                and not is_wall_btw(nr,nc,r,c):
                            diff = abs(A_anchor[r][c]-A_anchor[nr][nc])
                            A[r][c] -= diff//4
                            A[nr][nc] += diff//4

        #3 Side decrease
        for r in [0,R-1]:
            for c in range(C):
                if A[r][c]>0:
                    A[r][c]-=1
        for r in range(1,R-1):
            for c in [0,C-1]:
                if A[r][c]>0:
                    A[r][c]-=1

        #4 Check K
        end_flag=True
        for r,c in Z:
            if A[r][c]<K:
                end_flag=False
        if end_flag:
            return time_counter

    return time_counter+1   # 100 이후에도 종료X


print(solution())