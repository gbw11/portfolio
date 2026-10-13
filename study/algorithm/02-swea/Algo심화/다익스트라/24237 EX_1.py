graph = [[0]*6 for _ in range(6)]

graph[0][1] = 15
graph[0][2] = 17
graph[0][3] = 22
graph[1][2] = 5
graph[2][3] = 6
graph[2][4] = 2
graph[2][5] = 8
graph[3][5] = 7
graph[4][5] = 1

from heapq import heappop, heappush

def dijkstra(n):
    hq = [(0, n)]
    dists = [float('inf')]*6
    dists[0] = 0

    while hq:
        dist, now = heappop(hq)
        for i in range(6):
            if graph[now][i] != 0:
                new_dist = dist + graph[now][i]
                if dists[i] <= new_dist:
                    continue
                dists[i] = new_dist
                heappush(hq, (new_dist, i))

    return dists
ans = dijkstra(0)
print(*ans)
