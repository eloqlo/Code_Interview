def solution(intStrs, k, s, l):
    answer=[]
    for ele in intStrs:
        tmp=int(ele[s:s+l])
        if tmp>k:
            answer.append(tmp)
    return answer