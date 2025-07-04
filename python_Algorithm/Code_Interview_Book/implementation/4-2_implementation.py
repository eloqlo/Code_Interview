# 왕실의 나이트

def print_valid_move(coor):
    # 8 different moves. if result coor<1, that's not a valid move
    count = 0

    if coor[0]-2 > 0:
        # 좌로2가 유효하면
        if coor[1]-1 > 0:
            count += 1
        if coor[1]+1 < 8:
            count += 1
    if coor[0]+2 > 0:
        # 우로2가 유효하면
        if coor[1]-1 > 0:
            count += 1
        if coor[1]+1 < 8:
            count += 1
    if coor[1]-2 > 0:
        # 위로2가 유효하면
        if coor[0]-1 > 0:
            count += 1
        if coor[0]+1 < 8:
            count += 1
    if coor[1]+2 > 0:
        # 아래로2가 유효하면
        if coor[0]-1 > 0:
            count += 1
        if coor[0]+1 < 8:
            count += 1
        
    print(count)


if __name__ == '__main__':
    coor = input()
    coor_int = [0,0]
    
    if coor[0]=='a':
        coor_int[1] = 1
    elif coor[0]=='b':
        coor_int[1] = 2
    elif coor[0]=='c':
        coor_int[1] = 3
    elif coor[0]=='d':
        coor_int[1] = 4
    elif coor[0]=='e':
        coor_int[1] = 5
    elif coor[0]=='f':
        coor_int[1] = 6
    elif coor[0]=='g':
        coor_int[1] = 7
    elif coor[0]=='h':
        coor_int[1] = 8
    
    coor_int[0] = int(coor[1])
    
    print_valid_move(coor_int)