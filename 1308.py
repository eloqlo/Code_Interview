"""
윤년으로 input1이 들어오면 날짜 하루씩 덜 센다. 왜?
"""

# 입력 받아오기
input1 = list(map(int,input().split()))
input2 = list(map(int,input().split()))

m_normal = [31,28,31,30,31,30,31,31,30,31,30,31]
m_yun = [31,29,31,30,31,30,31,31,30,31,30,31]

# 연도 입력시 해당년도 전체 일수 반환 함수(윤년 고려)
def year_Counter(year: int):
    if year%4 == 0 :
        year_day = 366  # 이 아닌 4나 400으로 나눠떨어지는 윤년
        if year%100 == 0 and year%400 != 0 :
            year_day = 365  # 400으로 나눠떨어지지 않으면서 100으로 나눠떨어지는 평년
    else:
        year_day = 365  # 4로 안떨어지면 평년
    return year_day

# 사이 days 반환
def day_Counter(date1: list, date2: list):
    if date1[0] != date2[0]:    #1 입력된 연도 다르면
        # 남은 일수
        if year_Counter(date1[0])==365:
            m_passed = list(range(date1[1]-1, 12))
            days_passed_this_year = sum([m_normal[m] for m in m_passed])
            days1_left = days_passed_this_year - date1[2]
        else:
            m_passed = list(range(date1[1]-1, 12))
            days_passed_this_year = sum([m_yun[i] for i in m_passed])
            days1_left = days_passed_this_year - date1[2]
        
        # 사이 년도들 남은 일수
        years = list(range(input1[0]+1, input2[0]))  # 2009, 2010, ... , 2021    <-- 2008, 2022 입력됨
        days_count = 0
        for year in years:
            days_count += year_Counter(year)
        
        # 종료년도 지난날수
        if year_Counter(date2[0])==365:
            m_left = list(range(0,date2[1]-1))
            days_left_this_year = sum([m_normal[i] for i in m_left])
            days2_left = days_left_this_year + date2[2]
        else:
            m_left = list(range(0,date2[1]-1))
            days_left_this_year = sum([m_yun[i] for i in m_left])
            days2_left = days_left_this_year + date2[2]
            
        total_days = days1_left + days_count + days2_left
        # print(days1_left, days_count, days2_left)
        return total_days

    elif date1[0] == date2[0]:  #2 입력된 연도가 같으면
        total_days = year_Counter(date1[0])
        if total_days == 365:   
            m_passed = list(range(0,date1[1]-1))    # 해당월 미포함
            days_passed_this_year = sum([m_normal[i] for i in m_passed])
            days_passed = days_passed_this_year + date1[2]  # 해당월포함, 전체 지난 날들

            m_left = list(range(date2[1]-1, 12))    # 해당월 포함 남은 mounths
            days_left_this_year = sum([m_normal[m] for m in m_left])
            days_left = days_left_this_year - date2[2]    # 입력된 날짜 이후로 남은 날들

            return total_days - days_passed - days_left
        else:
            m_passed = list(range(0,date1[1]-1))    # 해당월 미포함
            days_passed_this_year = sum([m_yun[i] for i in m_passed])
            days_passed = days_passed_this_year + date1[2]  # 해당월포함, 전체 지난 날들

            m_left = list(range(date2[1]-1, 12))    # 해당월 포함 남은 mounths
            days_left_this_year = sum([m_yun[m] for m in m_left])
            days_left = days_left_this_year - date2[2]    # 입력된 날짜 이후로 남은 날들

            # print(total_days, days_passed, days_left)
            return total_days - days_passed - days_left

            
if __name__ == '__main__':
    if input2[0]-input1[0] > 1000 : # 1000년 이상 차이면 gg
        print('gg')
    elif input2[0]-input1[0] == 1000 and input1[1] > input2[1]: # 입력2의 월이 더 크면 gg
        print('gg')
    elif input2[0]-input1[0] == 1000 and input1[1] == input2[1] and input1[2]<=input2[2]: # 입력1,2 월 같을 때, 1의 일이 더 작거나같으면 gg
        print('gg')
    else:
        print( "D-" + str(day_Counter(input1, input2)) )


# 내 계산이 맞았다.
# 중간중간 실수랑, 변수명 헷갈려가지고 오류때문에 마지막에 많이 헤맸음.
# 경우의 수 따져서 하는게 맞았었군.