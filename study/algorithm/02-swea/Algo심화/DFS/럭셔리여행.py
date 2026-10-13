n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

depart, arrive = map(int, input().split())

visited = [False]*(n+1)

costs = []

def dfs(cur, cost):
    if cur == arrive:
        costs.append(cost)
        return
     
    visited[cur] = True

    for i in range(n):
        if graph[cur][i] != 0 and not visited[i]:
            dfs(i, cost + graph[cur][i])

    visited[cur] = False


dfs(depart, 0)

print(min(costs))
print(max(costs))