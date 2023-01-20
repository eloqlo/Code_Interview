# 이진수

# input
t = int(input())
n=[]
for _ in range(t):
    n.append(int(input()))

# 10진수 to 2진수 배열
def ten2two(ten):
    two=[]
    two_tmp =[]
    mok = ten//2
    if ten>1:
        mok = ten
        # two_tmp 라는 임시 이진수 배열을 구한다.
        while(mok>1):
            # mok을 계속 2로 나눠준다.
            # 그러면서 생기는 나머지를 tow_tmp에 저장한다.
            # 만일 mok이 1이되면 1을 two_tmp에 저장하고 BREAK
            # 만일 mok이 0이되면 BREAK
            namugi = mok%2
            mok = mok//2
            two_tmp.append(namugi)
            if mok==1:
                two_tmp.append(mok)
                break
            elif mok==0:
                break
        # 이진수로 만들어 반환, not for this task
        # for _ in range(len(two_tmp)):
        #     two.append(two_tmp.pop())
        # return two
        return two_tmp
            
    else:
        two.append(ten)
        return two

# loop : n에 대해 loop
for ten in n:
    #1 양의 정수를 이진수로 바꾼다
    two = ten2two(ten)

    #2 1의 위치를 저장한다/출력한다.
    for i, ele in enumerate(two):
        if ele==1:
            print(i, end=' ')