def solution(str_list, ex):
    li=''
    for ele in str_list:
        if ex in ele:
            continue
        li+=ele
    return li