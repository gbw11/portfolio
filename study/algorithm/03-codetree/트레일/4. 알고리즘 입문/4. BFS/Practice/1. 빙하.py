# 브루스포스 + dfs 이용한 풀이!( 시간초과에 걸림)

from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


# Please write your code here.

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def can_go(y, x, before):
    return in_range(y, x) and u <= abs(grid[y][x] - before) <= d

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]


def bfs(starts):
    q = deque()
    visited = [[False] * n for _ in range(n)]

    for y, x in starts:
        visited[y][x] = True
        q.append((y, x))

    # 출발점도 세기 때문에
    cnt = len(starts)

    while q:
        y, x = q.popleft()

        for dy, dx in zip(dys, dxs):
            ny = y + dy
            nx = x + dx

            if in_range(ny,nx) and not visited[ny][nx]:
                diff = abs(grid[y][x] - grid[ny][nx])
                if u <= diff <= d:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cnt += 1

    return cnt

cities = [(i, j) for i in range(n) for j in range(n)]

ans = 0
selected = []

# 조합 직접 구현(백트래킹)
def choose(start):
    global ans

    if len(selected) == k:
        ans = max(ans, bfs(selected))

    for i in range(start, n**2):
        selected.append(cities[i])
        choose(i + 1)
        selected.pop()

choose(0)

print(ans)
