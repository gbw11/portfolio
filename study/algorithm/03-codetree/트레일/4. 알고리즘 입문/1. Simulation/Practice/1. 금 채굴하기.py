n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def get_area(y, x, k, n): # y, x :중심점의 위치, k : 거리, n : 전체판 크기
    area = []
    for i in range(n):
        for j in range(n):
            if abs(y-i) + abs(x-j)<= k:
                area.append((i,j))

    return area

def find(y, x):
    global max_gold

    for k in range(2*n):
        area = get_area(y,x,k,n)
        cnt = sum(grid[i][j] for i, j in area)
        cost = k**2 + (k+1)**2
        gold = cnt * m
        if gold - cost >= 0:
            max_gold = max(max_gold, cnt)

max_gold = 0

for y in range(n):
    for x in range(n):
        find(y, x)

print(max_gold)