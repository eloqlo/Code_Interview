def solution(a, b):
    A = int(str(a)+str(b))
    B = int(str(b)+str(a))
    if A>B:
        return A
    else:
        return B