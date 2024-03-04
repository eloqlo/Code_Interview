def solution(q, r, code):
    answer = []
    
    for i in range(len(code)//q+1):
        idx=i*q+r
        if idx<len(code):
            answer.append(code[idx])
    
    return ''.join(answer)