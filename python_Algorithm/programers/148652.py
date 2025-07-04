def solution(n, l, r):
    #1 count quotient & remain for each level
    tmp_l={}
    tmp_r={}
    l_q=l-1
    r_q=r-1
    for i in range(n,0,-1):
        l_r= l_q%5
        l_q= l_q//5
        r_r= r_q%5
        r_q= r_q//5
        tmp_l[f'l{i}']=(l_q,l_r)
        tmp_r[f'r{i}']=(r_q,r_r)
    
    #2 count ones
    one_counter=0
    for exp, (l_qr, r_qr) in enumerate(zip(tmp_l.values(), tmp_r.values())):
        if exp!=n-1:
            l_add = 5-l_qr[1] if l_qr[1]>2 else 4-l_qr[1]
            l_add *= 4**exp
            r_add = r_qr[1]+1 if r_qr[1]<2 else r_qr[1]
            r_add *= 4**exp
            one_counter += l_add+r_add
        else:
            add_ = sum([1,1,0,1,1][l_qr[1]+1:r_qr[1]])
            one_counter += add_* 4**exp
    
    return one_counter

if __name__=="__main__":
    print(solution(2,4,17))