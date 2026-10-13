
y1, x1, y2, x2 = map(int, input().split())
i1, j1, i2, j2 = map(int, input().split())

# Please write your code here.

y1, x1, y2, x2 = y1+1000, x1+1000, y2+1000, x2+1000
i1, j1, i2, j2 = i1+1000, j1+1000, i2+1000, j2+1000


arr = [[0]*2000 for _ in range(2000)]

# 첫번째 사각형 범위에 1
for y in range(y1, y2):
    for x in range(x1, x2):
        arr[y][x] = 1

# 두번째 사각형 칠하면서 첫번째랑 겹치는 부분 지움
for i in range(i1, i2):
    for j in range(j1, j2):
        if arr[i][j] == 1:
            arr[i][j] = 0

# ==> 내가 가려야 할 곳에만 1이 존재하는중
# 제일 멀리 있는 값 정의하기!
xmin, ymin = 2001, 2001
xmax, ymax = -1, -1 # 배열의 최댓값

for y in range(y1, y2):
    for x in range(x1, x2):
        if arr[y][x] == 1:
            ymin = min(ymin, y)
            xmin = min(xmin, x)
            ymax = max(ymax, y)
            xmax = max(xmax, x)

if xmax < xmin or ymax < ymin:
    print(0)
else:
    result = (ymax-ymin+1)*(xmax-xmin+1)
    print(result)
