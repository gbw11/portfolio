from heapq import heappush, heappop

def dijkstra():
    hq = []
    # 비용과 좌표를 hq에 넣기
    heappush(hq, (0, 0, 0))

    costs = [[float('inf')]*n for _ in range(n)]
    costs[0][0] = 0

    while hq:
        cost, y, x = heappop(hq)

        if cost > costs[y][x]:
            continue
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny = y + dy
            nx = x + dx
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            diff = grid[ny][nx] - grid[y][x]
            if diff > 0:
                move_cost = diff*2
            elif diff == 0:
                move_cost = 1
            else:
                move_cost = 0
            new_cost = cost + move_cost
            if costs[ny][nx] <= new_cost:
                continue
            costs[ny][nx] = new_cost
            heappush(hq, (new_cost, ny, nx))
        for sy, sx, ey, ex, t_cost in teleport:
            if y == sy and x == sx: # 터널 입구에 있을 때
                new_cost = cost + t_cost
                if new_cost >= costs[ey][ex]:
                    continue
                costs[ey][ex] = new_cost
                heappush(hq, (new_cost, ey, ex))
    return costs[n-1][n-1]

t = int(input())

for tc in range(1, t+1):
    # n : 정방행렬의 크기, m : 터널의 갯수
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    # teleport : 터널이 좌표와 비용을 기록한 배열
    teleport = []
    for _ in range(m):
        sy, sx, ey, ex, c = map(int, input().split())
        sy, sx, ey, ex = sy-1, sx-1, ey-1, ex-1
        teleport.append((sy, sx, ey, ex, c))
        teleport.append((ey, ex, sy, sx, c))

    ans = dijkstra()
    print(f'#{tc}', ans)