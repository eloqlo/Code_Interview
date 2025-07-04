def solution(ni):
    nii = [ele.append(i+1) for i,ele in enumerate(ni)]  # make node number at 'index 3'
    nii.sort(key=lambda x: x[0])
    nii.sort(key=lambda x: x[1])
    
    #1 level별 묶음
    prev_y=0
    y=[]
    new_nii=[]
    for node in nii:
        if prev_y<node[1]:
            if len(y)!=0: 
                new_nii.append(y)
            y=[]
            prev_y=node[1]
        y.append(node)
    new_nii.append(y)
    # chunk: [x,y,node]
    # [[Lv1 chunks], [Lv2 chunks], ... ]
    
    #2 [[left_chid_node, right_child_node], ... ] 형태로 만들기
    """알고리즘 짜기"""
    
    
    #3 dfs
    
    answer = [[]]
    return answer