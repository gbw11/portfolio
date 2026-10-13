from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

dys = [-2, -1 , 1, 2, 2, 1, -1, -2]
dxs = [1, 2, 2, 1, -1, -2, -2, -1]


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

# 방문하지 못할시 -1 출력해야 하기 때문에 처음에 -1로 다 세팅하고 시작
visited = [[-1] * n for _ in range(n)]

def dfs(sy, sx):
    q = deque()
    visited[sy][sx] = 0
    q.append((sy, sx))


    while q:
        y, x = q.popleft()
        for dy, dx in zip(dys, dxs):
            ny = y + dy
            nx = x + dx

            if in_range(ny, nx) and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

dfs(r1, c1)

print(visited[r2][c2])