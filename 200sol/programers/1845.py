def solution(nums):
    
    table={}
    for ele in nums:
        if table.get(ele)==None:
            table[ele]=1
        else:
            table[ele]+=1
    N=len(nums)//2
    
    return min(N,len(table))