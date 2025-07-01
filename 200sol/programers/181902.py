def solution(my_string):
    anchor = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    answer = [0] * len(anchor)
    for ele in my_string:
        for idx in range(len(anchor)):
            if ele==anchor[idx]:
                break
        answer[idx]+=1
    return answer