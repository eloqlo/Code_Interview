def solution(m):
    a=[]
    for ele in m.split('x'):
        if ele!='':
            a.append(ele)
    a.sort()
    return a
