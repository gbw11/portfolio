commands = input()

# Please write your code here.
arr = [ch for ch in commands]

x, y = 0, 0

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

cnt = 0
idx = 0
for ch in arr:
    if ch == 'L':
        idx = (idx+3) % 4
        cnt +=1
    elif ch == 'R':
        idx = (idx+1) % 4
        cnt += 1
    if ch == 'F':
        x += dx[idx]
        y += dy[idx]
        cnt +=1

        if x==0 and y==0:
            print(cnt)
            exit()
print(-1)
