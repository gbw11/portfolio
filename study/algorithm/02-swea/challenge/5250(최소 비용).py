from heapq import heappush, heappop

def dijkstra():
    # dist, y, x
    hq = [(0, 0, 0)]

    dists = [[float('inf')]*n for _ in range(n)]
    dists[0][0] = 0

    while hq:
        dist, y, x = heappop(hq)

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            new_dist = dists[y][x] + max(grid[ny][nx] - grid[y][x], 0)+1

            if dists[ny][nx] <= new_dist:
                continue

            dists[ny][nx] = new_dist
            heappush(hq, (new_dist, ny, nx))

    return dists[n-1][n-1]

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    result = dijkstra()
    print(f'#{tc}', result)