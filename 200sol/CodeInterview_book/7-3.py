import sys

N,M = map(int,input().split())
li = list(map(int, sys.stdin.readline().rstrip().split()))
li.sort(reverse=True)   # O(NlogN)

H = M
H_prev = 0
counter_prev=0
for _ in range(N):
    norm = ele[0]-H
    counter = 0
    for ele in li:
        counter += ele-norm

    if counter==M:
        return H
    elif counter>M:
        H_new -= abs(H-H_prev)//2
        if H_new == H_prev:
            n1 = counter_prev-M
            n2 = counter-M
            if n1<n2 and n1>=0:
                return H_prev
            else:
                return H
        H_prev = H
        H = H_new
    elif counter<M:
        H_new += abs(H-H_prev)//2
        if H_new == H_prev:
            n1 = counter_prev-M
            n2 = counter-M
            if n1<n2 and n1>=0:
                return H_prev
            else:
                return H
        H_prev = H
        H = H_new