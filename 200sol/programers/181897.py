def solution(n, slicer, num_list):
    a,b,c=slicer
    if n==1:
        ans=num_list[:b+1]
    elif n==2:
        ans=num_list[a:]
    elif n==3:
        ans=num_list[a:b+1]
    elif n==4:
        ans=num_list[a:b+1:c]
    
    return ans