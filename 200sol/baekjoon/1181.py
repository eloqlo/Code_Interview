"""
merge sort
"""
import sys

n = int(sys.stdin.readline().strip())

words = []
for _ in range(n):
   w = sys.stdin.readline().strip()
   words.append(w)

# recursive 하게 작성할 수 있구나!
def merge_sort(unsorted_list):
   if len(unsorted_list)<=1:
      return unsorted_list

   # input을 반으로 나눈다.
   mid = len(unsorted_list)//2
   left = unsorted_list[:mid]
   right = unsorted_list[mid:]

   #  계속 recursive 하게 나누다가, 1칸이 되면, merge 시작해서 다 합쳐서 전부 다 합쳐서 반환한다.
   left_ = merge_sort(left)
   right_ = merge_sort(right)

   # 나뉜애를 정렬해 하나로 반환한다.
   return merge(left_, right_)

# 정렬된 왼쪽 리스트, 오른쪽 리스트를 크기순으로 병합한다.
def merge(left, right):
   i, j = 0, 0
   sorted_list = []

   while i<len(left) and j<len(right):
      # 왼 < 오
      if len(left[i]) < len(right[j]):
         sorted_list.append(left[i])
         i += 1
      # 왼단어 = 오단어
      elif left[i] == right[j]:
         sorted_list.append(right[j])
         j += 1
         i += 1
      # 왼 > 오
      else:
         sorted_list.append(right[j])
         j += 1

   # 남은놈들 plus
   while i < len(left):
      sorted_list.append(left[i])
      i += 1
   while j < len(right):
      sorted_list.append(right[j])
      j+= 1

   return sorted_list

""" 여기서 len<2 일때 뒤에꺼 씹힌다.
"""
def alphabet_sort(li):
   # 포인트 추출
   if len(li)>2:
      points = []
      for i in range(len(li)-1):
         if len(li[i]) < len(li[i+1]):
            points.append(i)  # 변하기 직전의 point 캐치
      
      sorted_list = []
      # 알파벳순 정렬
      for i in range(len(points)):
         if i==0: # 첫 points
            temp = li[:(points[i]+1)]
            temp.sort()
            sorted_list += temp
         elif i<len(points)-1: # 중간놈들
            temp = li[points[i-1]+1:(points[i]+1)]
            temp.sort()
            sorted_list += temp
         elif i == len(points)-1:  # 막놈들
            temp = li[points[i]:]
            temp.sort()
            sorted_list += temp
      
      return sorted_list
   else:
      return li
      
if __name__ == '__main__':
   words = set(words)
   words = list(words)
   words = merge_sort(words)  # 길이로 정렬
   words = alphabet_sort(words)  # 길이별 알파벳 순 정렬
   print('start!')
   for w in words:
      print(w)