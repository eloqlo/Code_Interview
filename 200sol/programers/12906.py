def solution(arr):
    prev_ele=None  
    ans=[]
    for ele in arr:
        if prev_ele != ele:
            ans.append(ele)
            prev_ele=ele
    return ans