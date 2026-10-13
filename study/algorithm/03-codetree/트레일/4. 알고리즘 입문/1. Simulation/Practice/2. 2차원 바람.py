n, m, q = map(int, input().split())

# Create 2D array for building state
arr = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

# 직사각형 테두리 시계방향으로 회전
def rotate(arr, r1, c1, r2, c2):
    coords = [] #1차원 배열에 테두리의 행열(위치)을 저장
    # 윗면
    for x in range(c1, c2): coords.append((r1,x))
    # 오른쪽
    for y in range(r1, r2): coords.append((y,c2))
    # 아래
    for x in range(c2, c1, -1): coords.append((r2,x))
    # 왼쪽
    for y in range(r2, r1, -1): coords.append((y,c1))

    values = [arr[y][x] for y, x in coords] # 위치에 맞는값 넣고
    values = [values[-1]] + values[:-1] # 시계방향 회전

    # 회전된 값 (values)를 원래의 위치(coords)에 넣기
    for (y, x), z in zip(coords, values):
        arr[y][x] = z


dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
# arr를 0부터 시작하기 위해서
for wind in winds:
    r1, c1, r2, c2 = wind[0] - 1, wind[1] - 1, wind[2] - 1, wind[3] -1

    rotate(arr,r1,c1,r2,c2) # 테두리 회전완료

    new_arr = [rows[:] for rows in arr] # 새로운 배열

# 직사각형 내부의 값들 평균값으로 변경 동시에!(새로운 배열에 새기기)

    for y in range(r1, r2+1):
        for x in range(c1, c2+1):
            urdl=[arr[y][x]] # 상하좌우 정보 담는 리스트/자기는 추가
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if not(0<=ny<n and 0<=nx<m): continue
                urdl.append(arr[ny][nx])
            new_arr[y][x] = sum(urdl) // len(urdl) #평균값 새기기

    arr = new_arr # 바뀐값을 기존 배열에 저장

for rows in arr:
    print(*rows)