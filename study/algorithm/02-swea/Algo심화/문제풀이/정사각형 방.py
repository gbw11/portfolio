from collections import deque

def bfs(sy,sx):
    q = deque()
    dist = [[0]*n for _ in range(n)]
    dist[sy][sx] = 1
    q.append((sy, sx))

    while q:
        y, x = q.popleft()

        for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if grid[ny][nx] == grid[y][x] + 1:
                    dist[ny][nx] = dist[y][x] +1
                    q.append((ny, nx))

    # 이동한 곳중에 제일 멀리 간 거 체크
    ans = max(max(rows) for rows in dist)

    # 시작점과 거리 리턴
    return grid[sy][sx], ans

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    result = ()
    for y in range(n):
        for x in range(n):
            pos, ans = bfs(y,x)
            # 거리가 더 크면 위치와 거리를 저장

            if ans>res:
                res = ans
                result = (pos, ans)
            # 거리의 최댓값이 같을 때 위치의 작은 수를 돌려준다.
            elif ans == res:
                if result[0]>pos:
                    result = (pos, ans)


    print(f'#{tc}', *result)