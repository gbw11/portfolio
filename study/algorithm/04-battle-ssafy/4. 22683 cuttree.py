import heapq

# 상하좌우
ydir = [-1, 1, 0, 0]
xdir = [0, 0, -1, 1]

# 방향 전환 비용
turnCnt = [
    [0, 2, 1, 1],  # 상
    [2, 0, 1, 1],  # 하
    [1, 1, 0, 2],  # 좌
    [1, 1, 2, 0]   # 우
]

INF = 21e8

def dijkstra(y, x):
    dist = [[[INF] * N for _ in range(N)] for _ in range(K + 1)]

    pq = []
    heapq.heappush(pq, (0, y, x, 0, K))  # (조작횟수, y, x, dir, 남은 벌목 횟수)

    while pq:
        controlCnt, y, x, dir, cutCnt = heapq.heappop(pq)

        # 전략 1. 더 큰 값 나오면 continue
        if dist[cutCnt][y][x] < controlCnt:
            continue

        # 4방향 탐색
        for i in range(4):
            ny = y + ydir[i]
            nx = x + xdir[i]
            nc = controlCnt + turnCnt[dir][i] + 1

            # 범위체크
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue

            # 나무인데 못 자르면 continue
            if board[ny][nx] == 'T' and cutCnt == 0:
                continue

            # 나무면 벌목 횟수 1 감소
            if board[ny][nx] == 'T':
                next_cutCnt = cutCnt - 1

                # 전략 2. 더 작은 값 나오면 갱신
                if dist[next_cutCnt][ny][nx] > nc:
                    dist[next_cutCnt][ny][nx] = nc
                    heapq.heappush(pq, (nc, ny, nx, i, next_cutCnt))

            else:
                next_cutCnt = cutCnt

                # 전략 2. 더 작은 값 나오면 갱신
                if dist[next_cutCnt][ny][nx] > nc:
                    dist[next_cutCnt][ny][nx] = nc
                    heapq.heappush(pq, (nc, ny, nx, i, next_cutCnt))

    result = INF
    for k in range(K + 1):
        result = min(result, dist[k][dy][dx])

    if result == INF:
        return -1
    return result


N, K = map(int, input().split())
board = []
sy = sx = dy = dx = -1

for i in range(N):
    row = list(input().strip())
    board.append(row)
    for j in range(N):
        if board[i][j] == 'X':
            sy, sx = i, j
        elif board[i][j] == 'Y':
            dy, dx = i, j

print(dijkstra(sy, sx))