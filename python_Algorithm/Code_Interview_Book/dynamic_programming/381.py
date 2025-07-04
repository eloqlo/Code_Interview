def is_in(arr, num):
    """
    ERROR CASE
    arr [1,2,3,4,5,6,0,0,0,0]
    num 6
    """
    st = 0
    ed = len(arr) - 1
    result = False
    for _ in range(len(arr) + 1):
        mid = (st+ed)//2
        if arr[mid] == num:
            result = True
            # print(f"----- 중복 생김 ------")
            break
        elif arr[mid] < num:
            st = mid + 1
        else:
            ed = mid - 1
        print("iteration")
        if st > ed:
            break
    return result

arr=[1,2,3,4,5,6,0,0,0,0]
num=6

is_in(arr,num)