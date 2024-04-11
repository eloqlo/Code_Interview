w1 = [int(ele) for ele in input()]
w2 = [int(ele) for ele in input()]
w3 = [int(ele) for ele in input()]
w4 = [int(ele) for ele in input()]
wheels=[w1,w2,w3,w4]
K = int(input())
rot_li=[]
for _ in range(K):
    num, direction = map(int,input().split())
    rot_li.append((num-1, direction))

debug_count=0
def rotate(wi, d):
    global wheels
    global debug_count
    debug_count+=1

    wheel= wheels[wi]
    if d==1:
        new_wheel = [wheel[-1]] + wheel[:-1]
    elif d==-1:
        new_wheel = wheel[1:] + [wheel[0]]
    else:
        raise
    wheels[wi] = new_wheel
    return wheel    # old wheel

def solution(debug):
    global wheels, rot_li, debug_count

    for wheel_idx, direction in rot_li:
        og_wheel = rotate(wheel_idx, direction)
        if debug:
            print("________")
            print(f"after wheel idx:{wheel_idx} rotation")
            for debug_idx in range(4):
                print(wheels[debug_idx])
                if debug_idx == wheel_idx:
                    print(" This one changed !")
            print()

        if wheel_idx==0:
            # check no.0
            if og_wheel[2]!=wheels[1][6]:
                old_wheel = rotate(wi=1, d= -direction)
                if debug:
                    print("________")
                    print(f"after wheel idx:{1} rotation")
                    for debug_idx in range(4):
                        print(wheels[debug_idx])
                        if debug_idx==1:
                            print(" This one changed !")
                    print()
                if old_wheel[2]!=wheels[2][6]:
                    old_wheel = rotate(wi=2, d=direction)
                    if debug:
                        print("________")
                        print(f"after wheel idx:{2} rotation")
                        for debug_idx in range(4):
                            print(wheels[debug_idx])
                            if debug_idx == 2:
                                print(" This one changed !")
                        print()
                    if old_wheel[2]!=wheels[3][6]:
                        _ = rotate(wi=3, d=-direction)
                        if debug:
                            print("________")
                            print(f"after wheel idx:{3} rotation")
                            for debug_idx in range(4):
                                print(wheels[debug_idx])
                                if debug_idx == 3:
                                    print(" This one changed !")
                            print()


        elif wheel_idx==1:
            # check no.1
            if wheels[0][2]!=og_wheel[6]:
                old_wheel=rotate(wi= 0,d= -direction)
                if debug:
                    print("________")
                    print(f"after wheel idx:{0} rotation")
                    for debug_idx in range(4):
                        print(wheels[debug_idx])
                        if debug_idx==0:
                            print(" This one changed !")
                    print()
            if og_wheel[2] != wheels[2][6]:
                old_wheel=rotate(wi= 2, d= -direction)
                if debug:
                    print("________")
                    print(f"after wheel idx:{2} rotation")
                    for debug_idx in range(4):
                        print(wheels[debug_idx])
                        if debug_idx==2:
                            print(" This one changed !")
                    print()
                if old_wheel[2] != wheels[3][6]:
                    _ = rotate(wi= 3, d= direction)
                    if debug:
                        print("________")
                        print(f"after wheel idx:{3} rotation")
                        for debug_idx in range(4):
                            print(wheels[debug_idx])
                            if debug_idx == 3:
                                print(" This one changed !")
                        print()
        elif wheel_idx==2:
            # check no.2
            if wheels[1][2] != og_wheel[6]:
                old_wheel = rotate(1,-direction)
                if debug:
                    print("________")
                    print(f"after wheel idx:{1} rotation")
                    for debug_idx in range(4):
                        print(wheels[debug_idx])
                        if debug_idx==1:
                            print(" This one changed !")
                    print()
                if wheels[0][2] != old_wheel[6]:
                    _=rotate(0, direction)
                    if debug:
                        print("________")
                        print(f"after wheel idx:{0} rotation")
                        for debug_idx in range(4):
                            print(wheels[debug_idx])
                            if debug_idx == 0:
                                print(" This one changed !")
                        print()
            if og_wheel[2]!=wheels[3][6]:
                _ = rotate(3, -direction)
                if debug:
                    print("________")
                    print(f"after wheel idx:{3} rotation")
                    for debug_idx in range(4):
                        print(wheels[debug_idx])
                        if debug_idx==3:
                            print(" This one changed !")
                    print()
        elif wheel_idx==3:
            # check no.3
            if wheels[2][2]!=og_wheel[6]:
                old_wheel = rotate(wi=2, d=-direction)
                if debug:
                    print("________")
                    print(f"after wheel idx:{2} rotation")
                    for debug_idx in range(4):
                        print(wheels[debug_idx])
                        if debug_idx==2:
                            print(" This one changed !")
                    print()
                if wheels[1][2]!=old_wheel[6]:
                    old_wheel = rotate(wi=1, d=direction)
                    if debug:
                        print("________")
                        print(f"after wheel idx:{1} rotation")
                        for debug_idx in range(4):
                            print(wheels[debug_idx])
                            if debug_idx == 1:
                                print(" This one changed !")
                        print()
                    if wheels[0][2]!=old_wheel[6]:
                        _=rotate(wi=0, d= -direction)
                        if debug:
                            print("________")
                            print(f"after wheel idx:{0} rotation")
                            for debug_idx in range(4):
                                print(wheels[debug_idx])
                                if debug_idx == 0:
                                    print(" This one changed !")
                            print()
        else:
            raise
    score = wheels[0][0]*1 + wheels[1][0]*2 + wheels[2][0]*4 + wheels[3][0]*8
    return score

print( solution(debug=False) )
# print("total rotations: ",debug_count)