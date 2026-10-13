from itertools import combinations

n = int(input())
grids = [list(input()) for _ in range(n)]

numbers = []
start = end = None

for y in range(n):
    for x in range(n):
        if grids[y][x] == 'S':
            start = (y, x)
        elif grids[y][x] == 'E':
            end = (y, x)
        elif grids[y][x].isdigit():
            numbers.append((int(grids[y][x]), y, x))

numbers.sort()

ans = float('inf')

for a, b, c in combinations(numbers, 3):
    if not (a[0] < b[0] < c[0]):
        continue

    dist = 0
    dist += abs(start[0] - a[1]) + abs(start[1] - a[2])
    dist += abs(a[1] - b[1]) + abs(a[2] - b[2])
    dist += abs(b[1] - c[1]) + abs(b[2] - c[2])
    dist += abs(c[1] - end[0]) + abs(c[2] - end[1])

    ans = min(ans, dist)

print(-1 if ans == float('inf') else ans)
