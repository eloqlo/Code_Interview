def solution(str1, str2):
    ans=''
    for s1,s2 in zip(str1,str2):
        ans+=s1+s2
        
    return ans