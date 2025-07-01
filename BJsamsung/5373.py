def solution(commands): #O(200)
    global cube
    side_dict={'U':0, 'F':1, 'L':2, 'B':3, 'R':4, 'D':5}

    for cmd in commands:
        si = side_dict[cmd[0]]
        di = cmd[1]
        prepared_sides = prepare_side(si)
        # change
        if di == '+':
            cube[si] = cw(cube[si])
            tmp = prepared_sides[0][0]
            prepared_sides[0][0] = prepared_sides[3][0]
            prepared_sides[3][0] = prepared_sides[2][0]
            prepared_sides[2][0] = prepared_sides[1][0]
            prepared_sides[1][0] = tmp
        else:
            cube[si] = ccw(cube[si])
            tmp = prepared_sides[0][0]
            prepared_sides[0][0] = prepared_sides[1][0]
            prepared_sides[1][0] = prepared_sides[2][0]
            prepared_sides[2][0] = prepared_sides[3][0]
            prepared_sides[3][0] = tmp
        revert_sides(prepared_sides, si)
def cw(side):
    return list(zip(*reversed(side)))
def ccw(side):
    tmp_side = [reversed(line) for line in side]
    return list(zip(*tmp_side))
def prepare_side(si):
    sod = [[1, 2, 3, 4],
           [5, 2, 0, 4],
           [5, 3, 0, 1],
           [5, 4, 0, 2],
           [5, 1, 0, 3],
           [3, 2, 1, 4]]
    so = sod[si]
    ps=[]
    if si==0:
        ps.append(cube[so[0]])
        ps.append(cube[so[1]])
        ps.append(cube[so[2]])
        ps.append(cube[so[3]])
    elif si==1:
        ps.append(cube[so[0]])
        ps.append(ccw(cube[so[1]]))
        ps.append(cw(cw(cube[so[2]])))
        ps.append(cw(cube[so[3]]))
    elif si==2:
        ps.append(cw(cube[so[0]]))
        ps.append(ccw(cube[so[1]]))
        ps.append(cw(cube[so[2]]))
        ps.append(cw(cube[so[3]]))
    elif si==3:
        ps.append(cw(cw(cube[so[0]])))
        ps.append(ccw(cube[so[1]]))
        ps.append(cube[so[2]])
        ps.append(cw(cube[so[3]]))
    elif si==4:
        ps.append(ccw(cube[so[0]]))
        ps.append(ccw(cube[so[1]]))
        ps.append(ccw(cube[so[2]]))
        ps.append(cw(cube[so[3]]))
    elif si==5:
        ps.append(cw(cw(cube[so[0]])))
        ps.append(cw(cw(cube[so[1]])))
        ps.append(cw(cw(cube[so[2]])))
        ps.append(cw(cw(cube[so[3]])))
    return ps

def revert_sides(ps, si):
    global cube
    sod = [[1, 2, 3, 4],
           [5, 2, 0, 4],
           [5, 3, 0, 1],
           [5, 4, 0, 2],
           [5, 1, 0, 3],
           [3, 2, 1, 4]]
    so=sod[si]
    if si==0:
        cube[so[0]] = ps[0]
        cube[so[1]] = ps[1]
        cube[so[2]] = ps[2]
        cube[so[3]] = ps[3]
    elif si==1:
        cube[so[0]] = ps[0]
        cube[so[1]] = cw(ps[1])
        cube[so[2]] = cw(cw(ps[2]))
        cube[so[3]] = ccw(ps[3])
    elif si==2:
        cube[so[0]] = ccw(ps[0])
        cube[so[1]] = cw(ps[1])
        cube[so[2]] = ccw(ps[2])
        cube[so[3]] = ccw(ps[3])
    elif si==3:
        cube[so[0]] = cw(cw(ps[0]))
        cube[so[1]] = cw(ps[1])
        cube[so[2]] = ps[2]
        cube[so[3]] = ccw(ps[3])
    elif si==4:
        cube[so[0]] = cw(ps[0])
        cube[so[1]] = cw(ps[1])
        cube[so[2]] = cw(ps[2])
        cube[so[3]] = ccw(ps[3])
    elif si==5:
        cube[so[0]] = cw(cw(ps[0]))
        cube[so[1]] = cw(cw(ps[1]))
        cube[so[2]] = cw(cw(ps[2]))
        cube[so[3]] = cw(cw(ps[3]))
    return

T = int(input())
cubes=[]
for test_case in range(T):
    # 위 앞 왼 뒤 오 아
    cube=[]
    for color in 'wrgoby':
        side = [[color]*3 for _ in range(3)]
        cube.append(side)
    n = int(input())
    commands=input().split()
    solution(commands)
    cubes.append(cube)


for test_case, cube in enumerate(cubes):
    for line in cube[0]:
        for ele in line:
            print(ele,end='')
        print()
