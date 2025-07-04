def solution(my_string, m, c):
    ans=[]
    for i in range(0,len(my_string),m):
        ans.append(my_string[i+(c-1)])
    return ''.join(ans)