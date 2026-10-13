graph = [
    [0,1,0,0,1],
    [0,0,0,1,1],
    [1,0,0,0,0],
    [1,0,1,0,0],
    [0,0,0,0,0]
]

s, e = map(int, input())

from collections import deque


def bfs(s):
    visited = [False] * 5
    q = deque()
    visited[s] = True
    q.append((s,0))

    while q:
        cur, dist = q.popleft()

        if cur == e:
            return dist

        for i in range(5):
            if graph[cur][i] == 1 and not visited[i]:
                visited[i] = True
                q.append((i, dist+1))
    return -1

print(bfs(s))
