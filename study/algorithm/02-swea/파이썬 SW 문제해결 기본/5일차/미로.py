T = int(input())
for test_case in range(1, T+1):
  n = int(input())
  arr = [list(map(int, input().strip())) for _ in range (n)]

  for i in range(n):
    for j in range(n):
      if arr[i][j] == 2: start = (i,j)
      elif arr[i][j] == 3: stop = (i,j)

  dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
  visited = [[False]*n for _ in range(n)]

  def dfs(arr, y, x):
    if arr[y][x] == 3:
      return 1

    visited[y][x] = True

    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if ny < 0 or ny >= n or nx < 0 or nx >= n:
        continue

      if arr[ny][nx] == 1 or visited[ny][nx]:
        continue

      if dfs(arr,ny, nx):
        return 1

    return 0
  print(f'#{test_case}', dfs(arr,start[0], start[1]))