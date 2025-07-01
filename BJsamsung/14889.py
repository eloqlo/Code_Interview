N = int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))
combinations1=[]
combinations2=[]

def set_combination1(idx, comb):
    # first combination
    global N, arr, combinations1

    if len(comb)==N//2:
        combinations1.append(comb)

    for ni in range(idx,N):
        set_combination1(ni+1, comb+[ni])

def set_combination2(idx, comb):
    # second combination
    global arr, combinations2, N

    if len(comb)==2:
        combinations2.append(comb)

    for ni in range(idx,N//2):
        set_combination2(ni+1, comb+[ni])

def solution():
    global N, arr, combinations1, combinations2
    min_diff = 1e+9

    for team1_comb in combinations1:

        team2_comb = []
        for idx in range(N):
            if idx in team1_comb:
                continue
            team2_comb.append(idx)

        team1_power = 0
        team2_power = 0
        for r,c in combinations2:
            nr = team1_comb[r]
            nc = team1_comb[c]
            team1_power += arr[nr][nc] + arr[nc][nr]

            nr = team2_comb[r]
            nc = team2_comb[c]
            team2_power += arr[nr][nc] + arr[nc][nr]

        min_diff = min(min_diff, abs(team1_power-team2_power))

    return min_diff

set_combination1(0,[])
set_combination2(0,[])

print(solution())