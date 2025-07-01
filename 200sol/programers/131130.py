def solution(cards):
    cards = list(map(lambda x:x-1, cards))
    hops=[]
    flag=False
    for _ in range(len(cards)):
        # 카드 다 조회했으면 끝.
        count=0
        for i,card in enumerate(cards):
            if card==None:
                count+=1
            if count==len(cards):
                flag=True
        if flag:
            break
        # None이 아닌 다음 card를 가져온다
        for card in cards:
            if card!=None:
                ptr=card
                break
        # 이번 hop 계산
        hop=[] 
        while cards[ptr]!=None:
            nxt_ptr=cards.pop(ptr)
            hop.append(ptr)
            cards.insert(ptr, None)
            ptr=nxt_ptr
        hops.append(hop)
    
    if len(hops)==1:
        answer=0
    else:
        hops = [len(hop) for hop in hops]
        hops.sort()
        answer = hops[-1]*hops[-2]
    
    return answer


if __name__=="__main__":
    li=[4,2,3,6,1,5]
    print(solution(li))