T = int(input())
for test_case in range(1, T+1):
  V, E = map(int, input().split())
  graph = dict()
  for i in range(1, V+1):
    graph[i] = []

  for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

  S, G = map(int, input().split())

  visited = [False] * (V+1)
  def dfs(node):
    if node not in graph:
      return

    visited[node] = True

    for nxt in graph[node]:
      if not visited[nxt]:
        dfs(nxt)

  dfs(S)
  if visited[G]:print(f"#{test_case} 1")
  else:print(f"#{test_case} 0")