def solution(answers):
    results = [0,0,0]
    man1_pattern=[1,2,3,4,5]
    man2_pattern=[2, 1, 2, 3, 2, 4, 2, 5]
    man3_pattern=[3,3,1,1,2,2,4,4,5,5]
    
    for idx, ans in enumerate(answers):
        if man1_pattern[idx%len(man1_pattern)]==ans:
            results[0]+=1
        if man2_pattern[idx%len(man2_pattern)]==ans:
            results[1]+=1
        if man3_pattern[idx%len(man3_pattern)]==ans:
            results[2]+=1
    
    ans=[]
    max_count=max(results)
    for i, result in enumerate(results):
        if result==max_count:
            ans.append(i+1)
    return ans