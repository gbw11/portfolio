from collections import deque
T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split()) # v 노드, e 간선
    
    graph = [[0] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    s, g = map(int, input().split())

    def bfs(start, goal):
        visited = [False] * (v+1)
        q = deque()
        visited[start] = True
        q.append((start, 0))

        while q:
            node, dist = q.popleft()
            if node == goal:
                return dist
            
            for x in graph[node]:
                if not visited[x]:
                    visited[x] = True
                    q.append((x, dist+1))
        return 0
    
    print(f'#{tc}', bfs(s, g))