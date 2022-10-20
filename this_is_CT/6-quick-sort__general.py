arr = [9,2,4,7,6,3,6,5,0,1,8]

def quick_sort(arr, start, end):
    if start>=end:    # 원소가 1개면 종료
        return          ## return 만으로 종료 가능하구나
    pivot = start   # 첫 원소를 피봇
    left = start + 1    # 첫 원소 옆이 left
    right = end     # 마지막이 right
    
    # 피봇 기준으로, 좌 우 정렬!
    while left <= right : 
        
        # left, right 피봇 걸리는 지점을 찾는다.
        while left <= end and arr[left]<=arr[pivot]:
            left+=1
        while right>start and arr[right]>=arr[pivot]:
            right-=1
        
        # 그 걸린 지점이,
        # left가 right 넘어서면
        if left>right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 넘은거 아니면, 둘이 바꿔주기
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

quick_sort(arr,0,len(arr)-1)
print(arr)