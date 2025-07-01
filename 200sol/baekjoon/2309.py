# input
hights = []
for _ in range(9):
    hights.append(int(input()))

# 함수정의
def finder(hights):
    for i1 in range(0,9):
        for i2 in range(1,9):
            if i1>=i2:
                continue
            result = sum(hights)-hights[i1]-hights[i2]
            if result==100:
                out = hights
                out.pop(i2)
                out.pop(i1)
                return out

# li = finder(hights).sort()
# for i in li:
#     print(i)