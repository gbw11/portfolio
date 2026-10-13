from heapq import heappop, heappush
# import sys
# sys.stdin = open('input.txt', "r")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dijkstra():
    # 누적거리, y, x
    pq = [(0, 0, 0)]
    # 최단거리를 저장할 2차원 리스트
    dists =[[float('inf')]*n for _ in range(n)]
    dists[0][0] = 0

    while pq:
        dist, y, x = heappop(pq)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 범위 밖이면 continue
            if ny< 0 or ny >= n or nx < 0 or nx >=n:
                continue
            # 누적거리 계산

            # 누적거리가 기존보다 크거나 같으면 continue
            new_dist = dist + graph[ny][nx]

            if dists[ny][nx] <= new_dist:
                continue
            # dist 갱신
            # pq에 저장
            dists[ny][nx] = new_dist
            heappush(pq, (new_dist, ny, nx))

    return dists[n-1][n-1]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # strip : 좌우 공백 없을때 사용
    graph = [list(map(int, input().strip())) for _ in range(n)]
    result = dijkstra()
    print(f'#{tc}', result)