def solution(s):
    sol=[]
    for ele in s:
        if 'ad' in ele:
            continue
        else:
            sol.append(ele)
    return sol