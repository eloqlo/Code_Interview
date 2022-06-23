"""
*** sorting ***
list를 돌면서 sort를 진행한다.
- insertion sort, selection sort, bubble sort, shell sort, quick sort, heap sort, merge sort 중
   merge sort(divide and conquer) 를 채택.
- 가장 복잡도가 작고 빨라서.
"""
import sys

n = int(sys.stdin.readline().strip())

words = []
for _ in range(n):
    w = sys.stdin.readline().strip()
    words.append(w)

