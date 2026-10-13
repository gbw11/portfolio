n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

graph = [[0] * (n + 1) for _ in range(n + 1)]
for r, c in edges:
    graph[r][c] = 1
    graph[c][r] = 1

visited = [0] * (n + 1)


cnt = 0
def dfs(vertex):
    global cnt
    for curr_v in range(1, n + 1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            visited[curr_v] = True
            cnt += 1
            dfs(curr_v)

# 처음 방문하는 곳 표시
visited[1] = 1      
dfs(1)
print(cnt)