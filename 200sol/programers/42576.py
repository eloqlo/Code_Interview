def solution(participant, completion):
    participant.sort(); completion.sort()
    completion.append('#END_CARD')
    for par, com in zip(participant, completion):
        if par != com:
            return par
