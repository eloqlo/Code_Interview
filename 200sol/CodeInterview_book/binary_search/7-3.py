# 떡의 개수, 요청 떡 길이
N, request_len = list(map(int, input().split()))
# 떡의 개별 높이 정보
array = list(map(int, input().split()))

st=0
ed=max(array)   # O(N)
result=0
for _ in range(N):
    mid= (st+ed)//2
    total=0
    
    for ele in array:
        if ele>mid:
            total+=ele-mid
    
    # 짧으면, 높이를 줄여야겠쥐?
    if total<request_len:
        ed = mid-1
        if st>ed:
            break
    elif total>request_len:
        result=mid   # 정답이 될 가능성이 있쥬?
        st = mid+1  # 범위를 높여서 간 봐볼까?
        if st>ed:
            break
    else:
        result = mid
        break

print(result)