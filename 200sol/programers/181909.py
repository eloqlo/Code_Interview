def solution(my_string):
    a = [my_string[-(i+1):] for i in range(len(my_string))]
    a.sort()
    return a