arr = [8,3,7,0,1,2,5,6,4,9]

def quick_sort(array):
    
    # 원소 없거나 하나면 return 해준다.
    if len(array)<=1:
        return array

    # 피봇이랑 tail 지정하고
    pivot = array[0]
    tail = array[1:]
    
    # 정리하고
    left_side = [x for x in tail if pivot>x]
    right_side = [x for x in tail if pivot<=x]
    
    # 그 정리한거를 다시 정리한다.
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(arr))