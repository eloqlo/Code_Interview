h,m,s = map(int, input().split())
# h,m,s = 14,20,0

t = int(input())
# t = 200
t_ = h*3600 + m*60 + s

t += t_

h_ = t//3600
m_ = t//60 - h_*60
s_ = t - h_*3600 - m_*60

print(h_%24, m_, s_)


# 몫 연산자와 나머지 연산자를 헷갈림