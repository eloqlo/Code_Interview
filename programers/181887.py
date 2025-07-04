def solution(num_list):
    s1= sum(num_list[0::2])
    s2= sum(num_list[1::2])
    return s1 if s1>s2 else s2