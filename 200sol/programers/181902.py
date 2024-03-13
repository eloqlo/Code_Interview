def solution(my_string):
    answer = [0 for _ in range(52)]
    
    for s in my_string:
        if ord(s)<97:
            answer[ord(s)-65] += 1
        else:
            answer[ord(s)-97+26] += 1
    
    return answer