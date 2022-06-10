input1 = list(map(int,input().split()))
input2 = list(map(int,input().split()))

m_normal = [31,28,31,30,31,30,31,31,30,31,30,31]
m_yun = [31,28,31,30,31,30,31,31,30,31,30,31]

# 연도 입력시 해당년도 전체 일수 반환
def year_Counter(year: int):
    year_day = 0
    if year%4 == 0 :
        if year%100 == 0 and year%400 != 0 :
            year_day = 365
        year_day = 366
    else:
        year_day = 365
    return year_day

# 사이 days 반환
def day_Counter(date1: list, date2:list):
    # 남은 일수
    if year_Counter(date1[0])==365:
        m_left = list(range(date1[1]-1, 12))
        days_left_this_year = sum([i for i in m_normal[m_left]])
        days1_left = days_left_this_year - date1[2]
    else:
        m_left = list(range(date1[1]-1, 12))
        days_left_this_year = sum([i for i in m_yun[m_left]])
        days1_left = days_left_this_year - date1[2]
    
    # 사이 년도들 남은 일수
    years = list(range(input1[0]+1, input2[0]))  # 2009, 2010, ... , 2021    <-- 2008, 2022 입력됨
    days_count = 0
    for year in years:
        days_count += year_Counter(year)
    
    # 종료년도 지난날수
    if year_Counter(date2[0])==365:
        m_left = list(range(0,date1[1]))
        days_left_this_year = sum([i for i in m_normal(m_left)])
        days2_left = days_left_this_year - date1[2]
    else:
        m_left = list(range(0,date1[1]))
        days_left_this_year = sum([i for i in m_yun(m_left)])
        days2_left = days_left_this_year - date1[2]
        
    total_days = days1_left + days_count + days2_left
    
    print(total_days)
    
    
if __name__ == '__main__':
    if input2[0]-input1[0] >= 1000:
        print('gg')
    else:
        print("D-" ,day_Counter(input1, input2))
