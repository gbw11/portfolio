from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# Please write your code here.


# 3차원 배열, 2차원 배열 위에 벽을 부순 횟수를 저장한다.
dist = [[[-1] * (k + 1) for _ in range(n)] for _ in range(n)]


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def bfs(sy, sx):
    q = deque()
    dist[sy][sx][0] = 0
    q.append((sy, sx, 0))

    while q:
        y, x, broken = q.popleft()

        if y == r2 and x == c2:
            return dist[y][x][broken]

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if not in_range(ny, nx):
                continue

            # 빈 칸
            if grid[ny][nx] == 0 and dist[ny][nx][broken] == -1:
                dist[ny][nx][broken] = dist[y][x][broken] + 1
                q.append((ny, nx, broken))

            # 벽인데 부술 수 있는 경우
            elif grid[ny][nx] == 1 and broken < k and dist[ny][nx][broken + 1] == -1:
                dist[ny][nx][broken + 1] = dist[y][x][broken] + 1
                q.append((ny, nx, broken + 1))

    return -1


print(bfs(r1, c1))