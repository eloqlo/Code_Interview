def solution(m):
    answer=''
    for ms in m:
        if ms<'l':
            ms='l'
        answer+=ms
    return answer