x,y,w,h = map(int, input().split())

result1 = min(x,w-x)
result2 = min(y,h-y)
result = min(result1, result2)

print(result)