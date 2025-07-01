import sys

input_val = sys.stdin.readline().strip()

cycle_len = 0

def cycle(numb:str):
    global cycle_len
    
    # 길이 짧으면 0붙이고
    if len(numb)<2:
        numb = '0'+numb
    
    # input 두 숫자 더하고
    n1, n2 = map(int, numb)
    output = n1 + n2
    
    # 기존 뒷자리랑 더한거 뒷자리 합쳐주고
    new_numb = str(n2)+str(output)[-1]
    cycle_len += 1
    if int(new_numb)==int(input_val):
        result = int(cycle_len)
        return result
    else:
        return cycle(new_numb)


print(cycle(input_val))