def solution(cards):
    cards = list(map(lambda x:x-1, cards))
    hops=[]
    unsearched_indices=[i for i in range(len(cards))]
    
    while len(unsearched_indices)==0:
        ptr=unsearched_indices[0]
        hop=[]
        while ptr!=False:
            unsearched_indices.pop(ptr)
            hop.append(cards.pop(ptr))
            cards.insert(ptr, False)
            ptr = cards[ptr]
        hops.append(hop)
    print(hops)
    if len(hops)==1:
        answer=0
    else:
        hops = [len(hop) for hop in hops]
        hops.sort()
        answer = hops[-1]*hops[-2]
    
    return answer