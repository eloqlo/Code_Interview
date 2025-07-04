N, L = map(int, input().split())
pd=[]
for _ in range(N):
    st,ed = map(int,input().split())
    pd.append([st,ed-1])  # 인덱스로 저장.
pd.sort()
pd.append((-1,-1))  # end flag

count = 0
st = pd[0][0]
for idx in range(N):
    pst, ped = pd[idx]
    pl = ped - pst + 1  # 웅덩이 길이
    X = pl//L + int(bool(pl%L)) # 필요 널빤지 개수

    if st <= pst:  # 이전 널빤지가 영향 X --> 새로 X개 놓기
        count += X
        st = pst + X*L
    elif st > pst:
        if ped <= st-1:     # 이전 널빤지가 지금꺼 다 덮음
            continue
        elif ped > st-1:    # 이전 널빤지가 지금꺼 부분 덮음
            pl = ped - st + 1
            X = pl//L + int(bool(pl%L))  # 필요 널빤지 개수

            count += X
            st += X*L

print(count)