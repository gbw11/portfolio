n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
# n : 격자크기, t : 시간, r,c : 초기 행,열 , d : 초기 방향
# Please write your code here.

arr = [[0] * n for _ in range(n)]

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

y, x = r - 1, c - 1

mapper = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3}

view = mapper[d]


def is_range(y, x):
    return 0 <= y < n and 0 <= x < n


cnt = 0
while cnt < t:
    y = y + dy[view]
    x = x + dx[view]
    cnt += 1
    if not is_range(y, x):
        y = y - dy[view]
        x = x - dx[view]
        view = (view + 2) % 4

print(y + 1, x + 1)