def solution(d1,d2):
    d1_int = int(str(d1[0]) + str(d1[1]) + str(d1[2]))
    d2_int = int(str(d2[0]) + str(d2[1]) + str(d2[2]))
    
    if d1_int<d2_int:
        return 1
    else:
        return 0