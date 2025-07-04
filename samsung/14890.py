N,L = map(int, input().split())
maps=[]
for _ in range(N):
    maps.append(list(map(int, input().split())))

def solution():
    global N,L, maps
    result = 2*N
    visit1 = [[0] * N for _ in range(N)]
    visit2 = [[0] * N for _ in range(N)]

    for line_idx, line in enumerate(maps):
        debug=False
        for idx in range(1,len(line)):
            if line[idx] - line[idx-1] == 1:    # 올라가
                tool = line[idx-L:idx]
                if len(tool)==L and len(set(tool))==1 and sum(visit1[line_idx][idx-L:idx])==0:
                    visit1[line_idx][idx-L:idx] = [1]*L
                    continue
                else:
                    result-=1
                    debug=True
                    break
            elif line[idx] - line[idx-1] == -1: # 내려가
                tool = line[idx:idx+L]
                if len(tool)==L and len(set(tool))==1:
                    visit1[line_idx][idx:idx+L] = [1]*L
                    continue
                else:
                    result-=1
                    debug = True
                    break
            elif line[idx] - line[idx-1] == 0:  # 평지
                continue
            else:
                result-=1
                debug = True
                break

        if debug:
            # print(f"____________line idx {line_idx}_____________")
            # print(line)
            # print()
            debug=False

    for line_idx, line in enumerate(zip(*maps)):
        debug = False
        for idx in range(1, len(line)):
            if line[idx] - line[idx-1] == 1:
                tool = line[idx-L:idx]
                if len(tool) == L and len(set(tool)) == 1 and sum(visit2[line_idx][idx - L:idx]) == 0:
                    visit2[line_idx][idx - L:idx] = [1] * L
                    continue
                else:
                    result -= 1
                    debug = True
                    break
            elif line[idx] - line[idx-1] == -1:
                tool = line[idx:idx+L]
                if len(tool) == L and len(set(tool)) == 1:
                    visit2[line_idx][idx:idx + L] = [1] * L
                    continue
                else:
                    result -= 1
                    debug = True
                    break
            elif line[idx] - line[idx - 1] == 0:
                continue
            else:
                result -= 1
                debug=True
                break

        if debug:
            # print(f"____________line idx {line_idx}_____________")
            # print(line)
            # print()
            debug = False


    return result

print(solution())