N, M, y, x, K = map(int,input().split())
x+=1
y+=1
world_map=[[-1]*(M+1)]
for _ in range(N):
    world_map.append([-1] + list(map(int,input().split())))
commands = list(map(int, input().split()))

def solution(commands):
    def _print_dice(dice, cmd, idx1, idx2, bottom_idx, top_idx):
        print(f"____________dice cmd:{cmd}______")
        print(f"____ Dice  val  /  idx ____")
        print(f"      {dice[idx1[3]]}       {idx1[3]}")
        print(f"    {dice[idx2[3]]} {dice[idx1[0]]} {dice[idx2[1]]}   {idx2[3]} {idx1[0]} {idx2[1]}")
        print(f"      {dice[idx1[1]]}       {idx1[1]}")
        print(f"      {dice[idx1[2]]}       {idx1[2]}")
        print()
        # print(f"____ Dice indies ____")
        # print(f"  {idx1[3]}  ")
        # print(f"{idx2[3]} {idx1[0]} {idx2[1]}")
        # print(f"  {idx1[1]}  ")
        # print(f"  {idx1[2]}  ")
        print()
        print("bottom idx: ", bottom_idx)
        print("top value: ", dice[top_idx])
        print("current x,y: ",x,y)
        print("_________________________________")
        print()

    global N, M, x, y, world_map
    idx1 = [1, 5, 6, 2]
    idx2 = [1, 3, 6, 4]
    dice = [-1, 0, 0, 0, 0, 0, 0]
    answer = []

    for cmd in commands:
        if cmd==1:  #동
            # change dice position in world_map
            if x==M:
                continue
                print("###")
            x += 1
            # change dice 전개도
            idx2 = idx2[1:]+[idx2[0]]
            idx1[0] = idx2[0]
            idx1[2] = idx2[2]
            # get dice index
            bottom_idx = idx1[0]
            top_idx = idx1[2]
        elif cmd==2:    #서
            # change dice position in world_map
            if x==1:
                continue
                print("###")
            x -= 1
            # change dice 전개도
            idx2 = [idx2[-1]] + idx2[:-1]
            idx1[0] = idx2[0]
            idx1[2] = idx2[2]
            # get dice index
            bottom_idx = idx1[0]
            top_idx = idx1[2]
        elif cmd==3:    #북
            # change dice position in world_map
            if y==1:
                continue
                print("###")
            y -= 1
            # change dice 전개도 수정
            idx1 = [idx1[-1]] + idx1[:-1]
            idx2[0] = idx1[0]
            idx2[2] = idx1[2]
            # get dice index
            bottom_idx = idx1[0]
            top_idx = idx1[2]
        elif cmd==4:    #남
            # change dice position in world_map
            if y==N:
                continue
                print("###")
            y += 1
            # change dice 전개도
            idx1 = idx1[1:] + [idx1[0]]
            idx2[0] = idx1[0]
            idx2[2] = idx1[2]
            # get dice index
            bottom_idx = idx1[0]
            top_idx = idx1[2]
        else:
            raise

        if world_map[y][x] == 0:
            world_map[y][x] = dice[bottom_idx]
        else:
            dice[bottom_idx] = world_map[y][x]
            world_map[y][x] = 0

        answer.append(dice[top_idx])

        # # Debug
        # _print_dice(dice, cmd, idx1, idx2, bottom_idx, top_idx)

    for ele in answer:
        print(ele)

solution(commands)