def solution(wallpaper):
    answer=[]
    min_x = 50
    min_y = 50
    max_x = 0
    max_y = 0
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x]=="#":
                if x<min_x:
                    min_x=x
                if y<min_y:
                    min_y=y
            if wallpaper[y][x]=="#":
                if x>max_x:
                    max_x=x
                if y>max_y:
                    max_y=y
    answer = [min_y,min_x,max_y+1,max_x+1]
    return answer