# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.

def compress(line):  # 0을 제외한 값들만 넣은 result를 정의하고 부족한 0은 뒤에 붙이는 함수

    arr = [x for x in line if x != 0]

    i = 0
    result = []

    while i < len(arr):
        if i + 1 <len(arr) and arr[i]==arr[i+1]:
            result.append(arr[i]*2)
            i += 2
        else:
            result.append(arr[i])
            i += 1

    return result + [0]*(4-len(result))

if dir == 'L':
    for i in range(4):
        grid[i] = compress(grid[i])

elif dir == 'R':
    for i in range(4):
        grid[i] = compress(grid[i][::-1])[::-1]

elif dir == 'U':
    for x in range(4):
        col = [grid[y][x] for y in range(4)] # 열들의 모임을  col에 저장
        col = compress(col) # 저장된 col을 함수에 넣고 돌림
        for i in range(4):
            grid[i][x] = col[i]

else:
    for x in range(4):
        col = [grid[y][x] for y in range(4)][::-1]
        col = compress(col)[::-1]
        for i in range(4):
            grid[i][x] = col[i]

for y in grid:
    print(*y)