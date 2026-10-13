n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 가장 큰 사각형 크기를 만들어서 grid를 돌면서 안에가 전부 양수인지 체크하고

def func(): # 잡은 범위 2개 안에서 음수 있으면 -1이고 다 양수면 넓이를 반환한다.0
    for a in range(y, i +1):
        for b in range(x, j +1):
            if grid[a][b] <= 0:
                return -1

    return (i+1-y)*(j+1-x)



value = -1
for y in range(n):
    for x in range(m):
        if grid[y][x] > 0 : # 양수인 지점 찾고
            for i in range(y, n): # 그거보다 우측아래 위치에서
                for j in range(x, m):
                    if grid[i][j] > 0: # 양수인 지점 찾고
                        value = max(value, func()) # 함수 돌린다.

print(value)



'''
# 재귀로 풀어봤으나 직사각형을 정의하지 못함(하지만 시도는 나쁘지 않았음)
check = [[False]*m for _ in range(n)] # 중복 체크 방지

def recur(y, x):
    if not(0 <= y < n and 0 <= x < m) or grid[y][x]<= 0: # 범위 벗어나거 음수면
        return 0

    if check[y][x]: # 이미 체크한 곳이여도
        return 0

    check[y][x] = True #호출되면 체크하고

    # 이렇게하면 직사각형이 아닌 연결된 모든 양수의 갯수를 세기는 함
    return 1 + (
        recur(y, x+1) + # 오른쪽
        recur(y+1, x) + # 아래쪽
        recur(y+1, x+1) # 대각선
    )


value = -1
for y in range(n):
    for x in range(m):
        value = max(value, recur(y, x))

print(value)
'''