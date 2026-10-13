mapping = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
}

graph = [[0] * 6 for _ in range(6)]
graph[0][1] = 5
graph[0][2] = 10
graph[0][3] = 7
graph[0][5] = 12
graph[1][0] = 5
graph[1][5] = 9
graph[2][5] = 1
graph[3][2] = 2
graph[3][4] = 1
graph[4][5] = 3

from heapq import heappop, heappush

start, end = input().split()
start = mapping[start]
end = mapping[end]

def dijkstra(start, end):
    dists = [float('inf')]*6
    dists[start] = 0
    hq = [(0, start)]

    while hq:
        dist, now = heappop(hq)
        for i in range(6):
            if graph[now][i] == 0:
                continue
            new_dist = dist + graph[now][i]
            if dists[i] <= new_dist:
                continue
            dists[i] = new_dist
            heappush(hq, (new_dist, i))
    return dists[end]

ans = dijkstra(start, end)
print(ans)