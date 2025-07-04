def solution(myStr):
    ans=myStr.replace('a',' ').replace('b',' ').replace('c',' ').split()
    if len(ans)==0:
        return ["EMPTY"]
    return ans