def solution(a, d, included):
    answer = 0
    
    for idx, ele in enumerate(range(a, a+d*(len(included)), d)):
        if included[idx]:
            answer+= ele
    
    return answer