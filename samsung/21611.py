def p(A):
    if type(A[0])!=list:
        for e in A:
            print(e,end=' ')
        print()
        return
    else:
        for l in A:
            for e in l:
                print(e, end=' ')
            print()
        print()
    print()

def solution():
    N,M = map(int,input().split())
    A=[]
    for _ in range(N):
        A.append(list(map(int,input().split())))
    magic=[]
    for _ in range(M):
        d,s = map(int,input().split())
        magic.append((d-1,s))
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]
    dr2=[0,1,0,-1]
    dc2=[-1,0,1,0]
    sr,sc = N//2, N//2
    ans=[0,0,0,0]

    for idx in range(M):
        d,s = magic[idx]

        #1.1 ice magic
        for s_iter in range(s):
            nr = sr + dr[d]*(s_iter+1)
            nc = sc + dc[d]*(s_iter+1)
            A[nr][nc] = 0

        #1.2 turn into 1d
        A_li = []
        break_flag = False
        iter_times = 1
        nr,nc = sr,sc

        for di in range(N*N):
            di = di%4
            tmp = []
            for _ in range(iter_times):
                nr,nc = nr+dr2[di], nc+dc2[di]
                if 0<=nr<N and 0<=nc<N:
                    if A[nr][nc]==0:
                        continue
                    tmp.append(A[nr][nc])
                else:
                    break_flag=True
                    break
            A_li += tmp     # ERROR FOUND
            if break_flag:
                break
            iter_times += di%2

        #2 pop marbles
        while True:
            break_flag = True
            tmp = []
            A_li_new = []
            for idx2, ele in enumerate(A_li):
                if idx2 == 0:
                    tmp.append(ele)
                    continue

                if ele == tmp[-1]:
                    tmp.append(ele)
                    continue
                if ele != tmp[-1]:
                    if len(tmp) >= 4:
                        break_flag = False
                        ans[tmp[-1]] += len(tmp)  # COUNT MARBLES
                        tmp = [ele]
                        continue
                    else:
                        A_li_new += tmp
                        tmp = [ele]
                        continue
            if len(tmp) < 4:
                A_li_new += tmp
                A_li = A_li_new
            else:
                # break_flag = False
                ans[tmp[-1]] += len(tmp)
            if break_flag:
                break

        if sum(A_li)==0:
            break

        #3.1 change marbles
        new_A_li = []
        prev_marble = A_li[0]
        count_same_marble=1
        for idx3 in range(1,len(A_li)):
            cur_marble = A_li[idx3]
            if prev_marble==cur_marble:
                count_same_marble+=1
            else:
                new_A_li+=[count_same_marble,prev_marble]
                prev_marble=cur_marble
                count_same_marble=1
        new_A_li+=[count_same_marble,prev_marble]
        A_li = new_A_li

        #3.2 1d to 2d
        A = [[0]*N for _ in range(N)]
        break_flag = False
        iter_times = 1
        nr, nc = N//2, N//2
        ali_idx = 0
        for di2 in range(len(A_li)):
            di = di2 % 4
            tmp = []
            for _ in range(iter_times):
                nr, nc = nr+dr2[di], nc+dc2[di]
                if 0 <= nr < N and 0 <= nc < N:
                    A[nr][nc] = A_li[ali_idx]
                    ali_idx+=1
                    if ali_idx==len(A_li):
                        break_flag=True
                        break
                else:
                    break_flag = True
                    break
            if break_flag:
                break
            iter_times += di % 2

    return ans[1] + ans[2]*2 + ans[3]*3

print(solution())

# T=int(input())
# results=[]
# for _ in range(T):
#     results.append(solution())
# for t in range(T):
#     print(f"#{t+1} {results[t]}")
#
#
# """
# 4
# 7 1
# 0 0 0 0 0 0 0
# 3 2 1 3 2 3 0
# 2 1 2 1 2 1 0
# 2 1 1 0 2 1 1
# 3 3 2 3 2 1 2
# 3 3 3 1 3 3 2
# 2 3 2 2 3 2 3
# 2 2
# 7 4
# 0 0 0 2 3 2 3
# 1 2 3 1 2 3 1
# 2 3 1 2 3 1 2
# 1 2 3 0 2 3 1
# 2 3 1 2 3 1 2
# 3 1 2 3 1 2 3
# 1 2 3 1 2 3 1
# 1 3
# 2 2
# 3 1
# 4 3
# 7 4
# 1 1 1 2 2 2 3
# 1 2 2 1 2 2 3
# 1 3 3 2 3 1 2
# 1 2 2 0 3 2 2
# 3 1 2 2 3 2 2
# 3 1 2 1 1 2 1
# 3 1 2 2 2 1 1
# 1 3
# 2 2
# 3 1
# 4 3
# 7 7
# 1 1 1 2 2 2 3
# 1 2 2 1 2 2 3
# 1 3 3 2 3 1 2
# 1 2 2 0 3 2 2
# 3 1 2 2 3 2 2
# 3 1 2 1 1 2 1
# 3 1 2 2 2 1 1
# 1 3
# 2 2
# 3 1
# 4 3
# 1 3
# 1 1
# 1 3
# """