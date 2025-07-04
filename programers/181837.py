def solution(order):
    answer = 0
    for o in order:
        if o[:3]=='ice' or o[:3]=='hot':
            o=o[3:]
        elif o[-3:]=='ice' or o[-3:]=='hot':
            o=o[:-3]
        
        if o=='americano' or o=='anything':
            answer+=4500
        else:
            answer+=5000
    
    return answer