def solution(array, commands):
    ans=[]
    for com in commands:
        tmp=array[com[0]-1:com[1]]
        tmp.sort()
        ans.append(tmp[com[2]-1])
    return ans