def solution(friends, gifts):
    arr = []
    dic = {}
    for i in range(len(friends)):
        arr.append([0] * len(friends))
        dic[friends[i]] = i

    rec = [0] * len(friends)
    for ele in gifts:
        f, t = ele.split()
        fn, tn = dic[f], dic[t]
        arr[fn][tn] += 1  # 준놈, 받은놈 업데이트
        rec[tn] += 1  # 받은 횟수

    for i in range(len(friends)):
        gift_val = sum(arr[i]) - rec[i]
        rec[i] = gift_val

    nxt_arr = [0] * len(friends)
    for a in range(len(friends) - 1):
        for b in range(a + 1, len(friends)):

            if (arr[a][b] > 0 or arr[b][a] > 0) and sum(arr[a]) != sum(arr[b]):  # 주고받은 기록이 있고, 둘이 횟수 달라
                if sum(arr[a]) < sum(arr[b]):
                    nxt_arr[b] += 1
                else:
                    nxt_arr[a] += 1
            else:
                # 선물지수
                if rec[a] < rec[b]:
                    nxt_arr[b] += 1
                elif rec[a] > rec[b]:
                    nxt_arr[a] += 1

    print(nxt_arr)
    return max(nxt_arr)