graph = [
    [0,7,20,8],
    [0,0,5,0],
    [15,0,0,0],
    [0,0,6,0]
]

n = int(input())

visited = [False]*4

costs = []
def dfs(curr, cost):
    global n
    if curr == n:
        costs.append(cost)

    visited[curr] = True

    for i in range(4):
        if graph[curr][i] != 0 and not visited[i]:
            dfs(i, cost + graph[curr][i])

    visited[curr] = False

dfs(0, 0)
print(*costs)