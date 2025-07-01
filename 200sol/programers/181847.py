def solution(n_str):
    for i in range(len(n_str)):
        if n_str[i]!='0':
            break
    return n_str[i:]
