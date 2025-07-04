def solution(ms, s, e):
    first = ms[:s]
    tmp=list(ms[s:e+1])
    tmp.reverse()
    mid = ''.join(tmp)
    end = ms[e+1:]
    return first+mid+end