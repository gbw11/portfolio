from heapq import heappush, heappop

def dijkstra():
    # dist, y, x
    pq = [(grid[0][0], 0, 0)]

    dists = [[float("inf")] * m for _ in range(n)]
    dists[0][0] = 0

    while pq:
        dist, y, x = heappop(pq)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= ny < n and 0 <= nx < m):
                continue
            new_dist = dist + grid[ny][nx]

            if dists[ny][nx] <= new_dist:
                continue
            dists[ny][nx] = new_dist
            heappush(pq, (new_dist, ny, nx))
    return dists[n - 1][m - 1]
n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

result = dijkstra()
print(result)

