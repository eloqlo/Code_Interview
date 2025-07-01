def solution(n):
    answer = ''
    for i in range(1,len(n)):
        logic=n[i]-n[i-1]
        if logic==1:
            answer+='w'
        elif logic==-1:
            answer+= 's'
        elif logic==10:
            answer+= 'd'
        elif logic==-10:
            answer+= 'a'
            
    return answer