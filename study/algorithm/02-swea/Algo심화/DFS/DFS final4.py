graph = [
    [0,2,6,3,0,0],
    [2,0,7,4,0,0],
    [6,7,0,0,0,0],
    [3,4,2,0,0,0],
    [0,0,1,0,0,7],
    [0,0,0,0,0,0]
]

a, b = map(int, input().split())

costs = []
visited = [False]*6

def dfs(cur, cost):
    if cur == b:
        costs.append(cost)
        return
    
    visited[cur] = True

    for i in range(6):
        if graph[cur][i] != 0 and not visited[i]:
            dfs(i, cost+graph[cur][i])
    visited[cur] = False

dfs(a, 0)

print(max(costs))
print(min(costs))