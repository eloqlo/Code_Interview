def solution(record):
    
    # raw data 정제
    id_dict={} # id:nickname
    final_message=[]
    for log in record:
        print(log)
        command, user_id, nickname = log.split()
        if command=='Enter':
            if user_id not in id_dict:
                id_dict[user_id] = nickname
            final_message.append((user_id,'enter'))
        if command=='Change':
            id_dict[user_id] = nickname
        if command=='Leave':
            final_message.append((user_id,'leave'))
    
    # 최종 결과 만들기
    answer=[]
    command_dict={'enter':'들어왔습니다.', 'leave':'나갔습니다.'}
    for user_id,command in final_message:
        answer.append(f"{id_dict[user_id]}님이 {command_dict[command]}")
    
    return answer