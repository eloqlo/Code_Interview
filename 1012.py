# 입력을 테스트케이스에 대해 list로 저장
t = int(input())
m=[0 for _ in range(t)]
n=[0 for _ in range(t)]
k=[0 for _ in range(t)]
pos=[[] for _ in range(t)]
passed=[[] for _ in range(t)]
for i in range(t):
    m[i],n[i],k[i] = map(int,input().split())
    for _ in range(k[i]):
        pos[i].append(list(map(int,input().split())))


# 각 테스트케이스에 대해 반복
for i in range(t):
    ans=[]
    ans.append(pos[i][0])   # 고립된 좌표들
    passed[i].append(pos[i][0])    # 첫 좌표 추가
    
    for p in pos[i][1:]:
        # 지나온애 내부중 새로운애의 상하좌우 겹치는지 조회
        flag=False
        if p[0] > 0:
            if [p[0]-1,p[1]] in passed[i]: flag=True
        if p[0] < m[i]-1:
            if [p[0]+1,p[1]] in passed[i]: flag=True
        if p[1] > 0:
            if [p[0],p[1]-1] in passed[i]: flag=True
        if p[1] < n[i]-1:
            if [p[0],p[1]+1] in passed[i]: flag=True
        passed[i].append(p) # 지나온 애들에 추가
        
        # 지나온 좌표들과 겹치지 않으면 ans에 추가
        if not flag:
            ans.append(p)
    # ans내부에서 겹치는지 확인
    real_ans=[]
    for p in ans:
        flag=False
        if p[0] > 0:
            if [p[0]-1,p[1]] in ans: flag=True
        if p[0] < m[i]-1:
            if [p[0]+1,p[1]] in ans: flag=True
        if p[1] > 0:
            if [p[0],p[1]-1] in ans: flag=True
        if p[1] < n[i]-1:
            if [p[0],p[1]+1] in ans: flag=True

        if not flag:
            real_ans.append(p)
    
    print(len(real_ans))
