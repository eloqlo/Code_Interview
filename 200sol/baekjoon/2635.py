"""
일일히 돌면서 count 하는 알고리즘. -> CORRECT

Debug Log
- 코드의 발상은 맞았지만, 구현 위치가 에러였다. 구현할때는 몰랐는데 코드 전체를 블록(기능)별로
- 조사해보니 굳이 여기에..? 부분에서 딱 오류가 나왔다.
1. 앞으로도, 짤때는 놓칠 수 있겠지만, 기능별 쓸모를 탐색해보며 찾을 수 있구나.
2. 주석의 기준이 매 코드가 아니라, 의미별로 달면 깔끔하구나
    - 근데도, 프로들은 주석 어떻게 달까? 생각했다. -> 클린코드! 언젠간 내 모든 코드에 
    - 클린코드까지 적용하는 날까지 레벨업 해야겠다!!!
3. 어제 안되던걸 해결하니 기분이 좋다! 여러 팁도 얻고 말이야!!

"""

# n = int(input())
# result=[]
#
# max_num = 0
# for num in range(1,n+1):
#
#     # 1부터 n까지 숫자를 전부 탐색
#     buffer=[n]
#     buffer.append(num)
#
#     # 규칙에 의거, 뺄샘 안될때까지 전수조사
#     for i in range(n):
#         try:
#             temp = buffer[i]-buffer[i+1]
#         except:
#             break
#         if temp >= 0:
#             buffer.append(temp)
#
#     if len(buffer) > max_num:   # 구현 코드의 위치가 문제였다!
#         max_num=len(buffer)
#         result=buffer
#
# print(len(result))
# for i in result:
#     print(i,end=' ')

def solution():
    N = int(input())
    max_arr=[]
    for num in range(N,0,-1):
        tmp_arr = [N, num]
        nxt_num = tmp_arr[-2] - tmp_arr[-1]
        while nxt_num >= 0:
            tmp_arr.append(nxt_num)
            nxt_num = tmp_arr[-2] - tmp_arr[-1]

        if len(max_arr)<len(tmp_arr):
            max_arr = tmp_arr

    print(len(max_arr))
    for ele in max_arr:
        print(ele, end=' ')

solution()