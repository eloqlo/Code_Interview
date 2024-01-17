def solution(s, pat):
    
    s=s.replace('A','C').replace('B','A').replace('C','B')
    return int(pat in s)