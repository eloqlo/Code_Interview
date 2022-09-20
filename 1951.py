n = input()

# 9 * (1 + 20 + 300 + 4000 + ...)
val_len = [i+1 for i in range(len(n))]
val_len.sort(reverse=True)

__sum=0
for val in n:
    _count=0
    _sum=0
    
    # 
    if val_len[0]!=1:
        for i in val_len:
            i -= 1
            _count += 9*i*(10**(i-1))
            _sum+=_count
    __sum += int(val)*_sum
    
print(__sum)