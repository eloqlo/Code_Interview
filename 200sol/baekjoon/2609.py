# 최대공약수, 최소공배수

# input
num1, num2 = map(int, input().split())

# functions
def yaksu(num):
    # O(N)
    li=[]
    for i in range(1,num+1):
        if num%i==0:
            li.append(i)
    return li

def func_min(n1, n2):
    # O(N^2)
    n1_li = yaksu(n1)
    n2_li = yaksu(n2)
    max_result=1
    for n1_ele in n1_li:
        for n2_ele in n2_li:
            if n1_ele==n2_ele:
                max_result = n1_ele
    return max_result


def soinsu(num):
    yaksu_list = yaksu(num)
    # num=1 인경우 따로 취급해주기
    soinsu_list=[]
    
    mok = num
    if num>1:
        for yaksu_element in yaksu_list:
            # 무한 loop 방지
            if yaksu_element==1:
                continue
            # 몫이 약수로 나눠떨어지면 약수저장 & 몫수정
            if mok % yaksu_element==0:
                soinsu = yaksu_element
                mok /= yaksu_element
                while(mok%yaksu_element==0):
                    soinsu *= yaksu_element
                    mok /= yaksu_element
                soinsu_list.append((yaksu_element,soinsu))                
        return soinsu_list
    else:
        soinsu_list.append(mok)
        return soinsu_list
    
def func_max1(n1, n2):
    n1_soinsu_list = soinsu(n1)
    n2_soinsu_list = soinsu(n2)
    result = 1
    divide = 1
    flag=True
    
    # O(N^2)
    # 최소공배수 계산
    for insu1, val1 in n1_soinsu_list:
        result*=val1
        for insu2, val2 in n2_soinsu_list:
            if insu1==insu2:
                divide*= min(val1,val2)
            if flag:
                result*=val2
        flag=False
        
    result /= divide
    
    return int(result)

def func_min2(n1,n2):
    value = 1
    result = 1
    # O(N)
    while(True):
        if value==min(n1,n2):
            if n1%value==0 and n2%value==0:
                result = value
            break
        if n1%value==0 and n2%value==0:
            result = value
        value+=1
    return result

def func_max2(n1, n2):
    value = max(n1, n2)
    
    # O(N)
    while(True):
        if value%n1==0 and value%n2==0:
            break
        value += 1
    return value

print(func_min2(num1,num2), func_max2(num1,num2), sep='\n')