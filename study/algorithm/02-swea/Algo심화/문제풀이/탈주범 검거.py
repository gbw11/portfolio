import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]
types = {
    1:[1,1,1,1],
    2:[1,1,0,0],
    3:[0,0,1,1],
    4:[1,0,0,1],
    5:[0,1,0,1],
    6:[0,1,1,0],
    7:[1,0,1,0],
}
from collections import deque

def bfs(r, c):
    visited[r][c] = 1
    q = deque([(r,c)])

    while q:
        y, x = q.popleft()
        dirs = types[graph[y][x]]
        # 현재 좌표로부터 갈 수 있는 모든 노드를 확인
        # 이동이 가능한 다음 좌표만 q에 추가
        for dir in range(4):
            # i 방향이 안뚫리면 못감
            if dirs[dir] == 0:
                continue
            ny = y + dy[dir]
            nx = x + dx[dir]

            #범위 밖이면 못감
            if ny <0 or ny >= n or nx<0 or nx>=m:
                continue
            # 방문했어도 못감, 0이어도 못감
            if visited[ny][nx] or graph[ny][nx]==0:
                continue

            # 다음 위치의 입구가 뚫려있는 곳으로만 이동 가능
            next_dirs = types[graph[ny][nx]]

            # 현재 상좌 -> 다음 방향의 하우가 안뚫리면 못감
            if dir %2 ==0 and next_dirs[dir+1]==0:
                continue
            # 현재 하우 -> 다음 방향의 상좌가 안뚫리면 못감
            if dir %2 ==1 and next_dirs[dir-1]==0:
                continue
            # l 시간을 넘어가면 안봐도 된다.
            if visited[ny][nx] + 1 > l:
                continue
            # 시간을 누적하면서 이동
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))

t = int(input())

for tc in range(1, t+1):
    n, m, r, c, l = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    bfs(r,c)

    cnt = 0

    for y in range(n):
        for x in range(m):
            if 0< visited[y][x] <=l:
                cnt+=1
    print(f'#{tc}', cnt)