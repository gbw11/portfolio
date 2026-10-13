n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input()) - 1


# Please write your code here.

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


# 시작 위치 찾는 방법
def get_start(k):
    if k // n == 0:  # 위에서 들어올때
        return 0, k, 2

    elif k // n == 1:  # 오른쪽에서 들어올때
        return k % n, n - 1, 3

    elif k // n == 2:  # 아래에서 들어올때
        return n - 1, (n - 1) - k % n, 0
    elif k // n == 3:  # 왼쪽에서 들어올때
        return (n - 1) - k % n, 0, 1


dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]


# 방향 전환 함수 정의
def turn(d, mirror):
    if mirror == '/':
        return {0: 1, 1: 0, 2: 3, 3: 2}[d]

    else:  # mirror = '\'
        return {0: 3, 3: 0, 2: 1, 1: 2}[d]


def simulation(y, x, d):
    cnt = 0
    while True:
        if not in_range(y, x):
            return cnt

        if grid[y][x] in ('/', '\\'):
            d = turn(d, grid[y][x])

        y += dy[d]
        x += dx[d]
        cnt += 1


y, x, d = get_start(k)
print(simulation(y, x, d))