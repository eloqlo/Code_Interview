arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12]]

arr_90 = list(map(list, zip(*arr[::-1])))
print(arr_90)

tmp_arr=[ele[::-1] for ele in arr]
arr_minus90 = list(map(list, zip(*tmp_arr)))
print((arr_minus90))