# https://school.programmers.co.kr/learn/courses/30/lessons/42627
def solution(jobs):
    jobs.sort(key=lambda x:x[0])  #! 1
    time_counter=0
    job_len = len(jobs)
    
    for i in range(job_len):
        if i==0:
            job=jobs.pop(0)
            now_time=job[0]+job[1]   # 방금 처리된 작업 종료 시각
            time_counter += job[0]+job[1]
            continue
        
        min_process_time=1000
        idx = False
        # 처리하는 동안 쌓인애들 중 짧은 실행시간인 프로세스 위치 찾기
        for j in range(len(jobs)):
            if jobs[j][1]<min_process_time and jobs[j][0]<now_time:
                min_process_time = jobs[j][1]
                idx=j
        # 만일 처리하는 동안 작업이 없었으면, 그 다음 들어오는 작업을 처리
        if idx==False:
            idx = 0
        
        # 다음 실행할 놈 리스트에서 제거 / 전체 소요시간 업데이트 / 현재시각 업데이트
        job=jobs.pop(idx)
        time_counter += (now_time-job[0]) + job[1]
        now_time += job[1]
        
    answer = time_counter//job_len
    return answer

if __name__=="__main__":
    jobs = [[0, 3], [1, 9], [2, 6]]
    print(solution(jobs))
    
    
    
"""
< 어려운 점(감정 빼고 돌아보기) >

1. 어떻게 풀어야 할지 감은 잡히는데, 구현이 어렵다. 뭐가 문제일까?
2. 푸는 과정이 깔끔하지 않다.
3. 풀이시간이 오래걸린다.(4시간)

>>> 오랜만에 풀은 두번째 문제였던 만큼, 휘둘리지 말고 10개는 풀어보고 생각하자.
"""