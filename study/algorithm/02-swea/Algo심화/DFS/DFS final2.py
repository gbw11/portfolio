graph = [
    [0,2,6,3,0,0],
    [2,0,7,4,0,0],
    [6,7,0,0,0,0],
    [3,4,2,0,0,0],
    [0,0,1,0,0,7],
    [0,0,0,0,0,0]
]


visited = [False] * 6

def dfs(curr):
    print(curr, end = ' ')
    visited[curr] = True

    for i in range(6):
        if graph[curr][i]==0 or visited[i]:
            continue
        dfs(i)
    visited[curr] = False

dfs(4)