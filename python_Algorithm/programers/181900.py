def solution(ms, ids):
    ids.sort()
    for k in range(len(ids)):
        ids[k]-=k
    ans_list = list(ms)
    for i in range(len(ids)):
        ans_list.pop(ids[i])
    return ''.join(ans_list)