def solution(friends, gifts):
    arr = []  # n이 a-z 누구에게 몇번 줬는지
    dic = {}  # dictionary
    back_dic = {}
    for i in range(len(friends)):
        arr.append([0] * len(friends))
        dic[friends[i]] = i
        back_dic[i] = friends[i]

    rec = [0] * len(friends)  # n이 누구에게 받았는지
    for ele in gifts:
        f, t = ele.split()
        fn, tn = dic[f], dic[t]
        arr[fn][tn] += 1  # 준놈, 받은놈 업데이트
        rec[tn] += 1  # 받은 횟수

    # 선물 지수 계산
    for i in range(len(friends)):
        gift_val = sum(arr[i]) - rec[i]
        rec[i] = gift_val

    nxt_arr = [0] * len(friends)
    for a in range(len(friends) - 1):
        for b in range(a + 1, len(friends)):

            # 주고받은 기록이 있고 && 주고받은 횟수가 다름
            if (arr[a][b] > 0 or arr[b][a] > 0) and arr[a][b] != arr[b][a]:
                if arr[a][b] < arr[b][a]:
                    nxt_arr[b] += 1
                elif arr[a][b] > arr[b][a]:
                    nxt_arr[a] += 1
            # 선물지수 비교
            else:
                if rec[a] > rec[b]:
                    nxt_arr[a] += 1
                elif rec[a] < rec[b]:
                    nxt_arr[b] += 1

    return max(nxt_arr)