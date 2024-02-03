def solution(myString, pat):
    ans=''
    for idx in range(len(myString),len(pat)-1,-1):
        if myString[idx-len(pat):idx] == pat:
            ans = myString[:idx]
            break
    return ans