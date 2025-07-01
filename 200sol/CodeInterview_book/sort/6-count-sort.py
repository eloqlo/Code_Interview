# p171
# Count Sort : 시작숫자와 끝숫자의 격차가 너무 크지 않은 상황 + 원소들이 모두 양의 정수 인 경우 기발한 정렬방법

unsorted = [0,5,2,7,4,8,9,3,6,5,6,3,1,4,4,7,2,6,2,2,2,0,9,1,3]

tmp = [0]*(max(unsorted)+1)

for element in unsorted:
   tmp[element] += 1

for i, element in enumerate(tmp):
    if element!=0:
        for _ in range(element):
            print(i, end='')
        print(end=' ')  # 00 11 22222 333 444 55 666 77 8 99