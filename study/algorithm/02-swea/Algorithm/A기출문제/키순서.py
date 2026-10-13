from collections import deque

def bfs(start, graph):
    visited = [False]*(n+1)
    q = deque([start])
    visited[start] = True
    cnt = 0

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                cnt += 1
                q.append(nxt)

    return cnt

T = int(input())

for tc in range(1, T+1):

    n = int(input())
    m = int(input())

    # 나보다 큰 학생
    graph = [[] for _ in range(n+1)]
    
    # 나보다 작은 학생
    rgraph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        # 나보다 작은 학생의 그래프 임으로 
        rgraph[b].append(a)

    ans = 0

    for i in range(1, n+1):

        bigger = bfs(i, graph)
        smaller = bfs(i, rgraph)
        
        # 큰학생 + 작은학생 == 전체-나 이면 내 위치 알 수 있음
        if bigger + smaller == n-1:
            ans += 1

    print(f"#{tc} {ans}")