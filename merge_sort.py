li = [37,10,22,30,35,13,25,24,1,0,-1,-20,51,37,99,12,0,1,3,7,5,1,9,8,4,44,2,46,37,98,100]

# recursive 하게 작성할 수 있구나!
def merge_sort(unsorted_list):
    if len(unsorted_list)<=1:
        return unsorted_list
    
    # input을 반으로 나눈다.
    mid = len(unsorted_list)//2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]
    
    # 계속 recursive 하게 나누다가, 1칸이 되면, merge 시작해서 다 합쳐서 전부 다 합쳐서 반환한다.
    left_ = merge_sort(left)
    right_ = merge_sort(right)
    
    # 나뉜애를 정렬해 하나로 반환한다.
    return merge(left_, right_)

# 정렬된 왼쪽 리스트, 오른쪽 리스트를 크기순으로 병합한다.
def merge(left, right):
    i, j = 0, 0
    sorted_list = []
    
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j+= 1
    return sorted_list
print(merge_sort(li))