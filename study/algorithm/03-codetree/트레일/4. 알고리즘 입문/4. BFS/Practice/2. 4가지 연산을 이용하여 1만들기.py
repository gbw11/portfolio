from collections import deque

N = int(input())

# Please write your code here.

dist = [-1] * 1000001


def dfs(start):
    q = deque()
    dist[start] = 0
    q.append(start)

    while q:
        n = q.popleft()

        if n == 1:
            return dist[n]

        for nxt in (n - 1, n + 1):
            if 0 <= nxt <= 1000000 and dist[nxt] == -1:
                dist[nxt] = dist[n] + 1
                q.append(nxt)

        if n % 2 == 0:
            nxt = n // 2
            if dist[nxt] == -1:
                dist[nxt] = dist[n] + 1
                q.append(nxt)

        if n % 3 == 0:
            nxt = n // 3
            if dist[nxt] == -1:
                dist[nxt] = dist[n] + 1
                q.append(nxt)


print(dfs(N))