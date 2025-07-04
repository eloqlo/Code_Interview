    def solution(citations):
    answer=[0]*10001
    
    for ele in citations:
        for i in range(ele+1):
            answer[i]+=1
    h=1
    for i, citation in enumerate(answer):
        if i>citation:
            break
        h=i
    
    return h