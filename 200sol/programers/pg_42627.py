# https://school.programmers.co.kr/learn/courses/30/lessons/42627
"""
disk controler
"""
def my_solution(jobs):
    jobs.sort(key=lambda x:(x[0],x[1]))   # 요청시각, 짧은 수행시간 으로 정렬
    time_counter=0
    
    print(jobs)
    
    # process initial task
    job_len = len(jobs)
    job=jobs.pop(0)
    now_time=job[0]+job[1]   # 방금 처리된 작업 종료 시각
    time_counter += job[1]
    # 순차적으로 처리하는 알고리즘
    for i in range(job_len-1):
        none_flag=False
        #1 다음 실행할 프로세스 index 찾기
        min_process_time=1001
        idx = 'none'
        for j in range(len(jobs)):
            if jobs[j][1]<min_process_time and jobs[j][0]<now_time:
                min_process_time = jobs[j][1]
                idx=j
        if idx=='none':
            idx = 0
            none_flag=True
        #2 다음 실행할 놈 리스트에서 제거 / 전체 소요시간 업데이트 / 현재시각 업데이트
        job=jobs.pop(idx)
        if none_flag:
            time_counter += job[1]
            now_time += job[1]+(job[0]-now_time)
        else:
            time_counter += (now_time-job[0]) + job[1]  # 기다린시간 + 수행시간
            now_time += job[1]  #
    answer = time_counter//job_len
    return answer