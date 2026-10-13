from collections import deque

n, m = map(int, input().split())

graph = list([] for _ in range(n))

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    graph[a].append(b)
    graph[b].append(a)

# r 시작지점, k 탑승횟수
r, k = map(int, input().split())

visited = [False]*n
q = deque()
q.append((r,0))
visited[r] = True

ans = 0
while q:
    now, cnt = q.popleft()
    if cnt <= k:
        ans += 1
        
    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, cnt+1))

print(ans)