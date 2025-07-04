from collections import defaultdict

def solution():
    N = int(input())
    lines={}
    for idx in range(N):
        a,b = map(int,input().split())
        lines[a] = b

    # total_lines = len(lines)
    # for count in range(total_lines):
    #     # 각 위치별 꼬인 애들 파악
    #     cur_st_loc = sorted(list(lines.keys()))
    #     cur_crossed = defaultdict(int)
    #
    #     for idx, st in enumerate(cur_st_loc):
    #         for tmp_st in cur_st_loc[idx+1:]:
    #             if lines[tmp_st]<lines[st]:
    #                 cur_crossed[st]+=1
    #                 cur_crossed[tmp_st]+=1
    #
    #     max_val=0
    #     max_key=None
    #     for key in cur_crossed:
    #         if max_val<cur_crossed[key]:
    #             max_val = cur_crossed[key]
    #             max_key = key
    #     if max_key==None:
    #         break
    #     lines.pop(max_key)

    count=0
    B = []
    for a in sorted(list(lines.keys())):
        B.append(lines[a])



    return count

print(solution())