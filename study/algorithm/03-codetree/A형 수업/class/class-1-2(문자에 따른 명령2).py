dirs = input()

# Please write your code here.

x, y = 0, 0

arr = [ch for ch in dirs]



dx, dy = [0, 1, 0, -1], [1, 0 , -1, 0]

dir_num = 0
for ch in arr :
    if ch == "L":
        dir_num = (dir_num +3) % 4
    elif ch == "R":
        dir_num = (dir_num+1) % 4
    else :
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)