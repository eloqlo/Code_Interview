
N,M,K = map(int,input().split())
arr=[[5]*N for _ in range(N)]
A=[]
tree={}
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(M):
    r,c,age = map(int,input().split())
    tree[(r-1,c-1)] = [age]

dr=[-1,-1,0,1,1,1,0,-1]
dc=[0,1,1,1,0,-1,-1,-1]

for _ in range(K):
    new_tree = {}
    for original_r in range(N):
        for original_c in range(N):

            if (original_r, original_c) in tree:
                r = original_r
                c = original_c

                will_be_new_trees=0
                new_age = []
                neut = 0
                for idx in range(len(tree[(r,c)])):
                    age = tree[(r,c)][idx]
                    if arr[r][c] >= age:
                        arr[r][c] -= age
                        new_age.append(age+1)
                        if (age+1)%5==0:
                            will_be_new_trees+=1
                    else:
                        neut += age//2
                arr[r][c] += neut

                # 나무가 다 죽으면, 번식 생략
                if (r,c) not in new_tree:
                    if not len(new_age)==0:
                        new_tree[(r,c)] = new_age
                else:
                    new_tree[(r,c)] += new_age

                # 나무의 번식
                for di in range(8):
                    nr, nc = r+dr[di], c+dc[di]
                    if 0<=nr<N and 0<=nc<N:
                        if (nr,nc) not in new_tree:
                            new_tree[(nr,nc)] = [1]*will_be_new_trees
                        else:
                            new_tree[(nr,nc)] = [1]*will_be_new_trees + new_tree[(nr,nc)]

            arr[original_r][original_c] += A[original_r][original_c]
    tree = new_tree
    # print(tree)

result = 0
for vals in tree.values():
    result += len(vals)

print(result)