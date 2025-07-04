# bronze 1
day_list = ["SUN",'MON','TUE',"WED","THU",'FRI','SAT']
mounth = [31,28,31,30,31,30,31,31,30,31,30,31]
plus = 0
mon, day = map(int, input().split())    # mounth, day

for i in range(mon-1):
    plus += mounth[i]

print(day_list[(day + plus)%7])