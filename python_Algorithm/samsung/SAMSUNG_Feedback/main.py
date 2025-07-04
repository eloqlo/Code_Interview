def test(n1,n2):
    global N
    return n1+n2+N

if __name__=="__main__":
    N=3
    print(test(1,2))