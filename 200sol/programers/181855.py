def solution(strArr):
    ansList=[0]*31
    for ele in strArr:
        ansList[len(ele)]+=1
    return max(ansList)