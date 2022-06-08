X = [1,2,3,4,5,6]
X2 = []

for i in range(1,7):
    Y = []
    for j in range(1,7):
        Y.append((i+j)**2)
    X2.append(Y)

print(X2)

sum=0

for elements in X2:
    for element in elements:
        sum += element

print(sum/36)