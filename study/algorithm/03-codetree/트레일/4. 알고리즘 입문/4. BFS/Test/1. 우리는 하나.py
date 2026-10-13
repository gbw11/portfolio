from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

# 방문 기록 전역으로
visited = [[False] * n for _ in range(n)]

dys = [-1, 1, 0, 0]
dxs = [0, 0, 1, -1]

# 연결된 도시들의 수를 저장하는 배열
components = []

for y in range(n):
    for x in range(n):
        # 방문하지 않은 점이면 그 점에서 연결된 도시 다 체크
        if not visited[y][x]:
            q = deque()
            q.append((y, x))
            visited[y][x] = True
            # 연결 도시들의 갯수를 체크하기 위함(본인 포함)
            size = 1

            while q:
                y, x = q.popleft()

                for dy, dx in zip(dys, dxs):
                    ny = y + dy
                    nx = x + dx
                    if in_range(ny, nx) and not visited[ny][nx]:
                        diff = abs(grid[y][x] - grid[ny][nx])
                        if u <= diff <= d:
                            # 중복 확인하지 않기 위해 연결된 점들도 방문 체크
                            visited[ny][nx] = True
                            q.append((ny, nx))
                            size += 1

            components.append(size)

components.sort(reverse = True)

print(sum(components[:k]))

# 위 코드는 연결된 components 들의 크기를 구해서 넣은다음에 그 안에서 연결된 애들은 어차피 다 같은 값이기 때문에 탐색을 안함
# 아래 코드는 모든 점 중에서 k개의 점을 조합으로 고르고 그 점들에 대해서 bfs를 진행한 다음에 합을 구한다음 그 합등중의 최댓값을 보냄
# 시간복잡도 높아서 시간 초과 뜨는 방식 브루트포스 & BFS

from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


# Please write your code here.

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def can_go(y, x, before):
    return in_range(y, x) and u <= abs(grid[y][x] - before) <= d

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]


def bfs(starts):
    q = deque()
    visited = [[False]* n for _ in range(n)]
    
    for y, x in starts:
        visited[y][x] = True
        q.append((y, x))
    
    # 출발점도 세기 때문에
    cnt = len(starts)
    
    while q:
        y, x = q.popleft()

        for dy, dx in zip(dys, dxs):
            ny = y + dy
            nx = x + dx

            if in_range(ny,nx) and not visited[ny][nx]:
                diff = abs(grid[y][x] - grid[ny][nx])
                if u <= diff <= d:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cnt += 1
                    
    return cnt

cities = [(i, j) for i in range(n) for j in range(n)]

ans = 0
selected = []

# 조합 직접 구현(백트래킹)
def choose(start):
    global ans
    
    if len(selected) == k:
        ans = max(ans, bfs(selected))
        
    for i in range(start, n**2):
        selected.append(cities[i])
        choose(i + 1)
        selected.pop()

choose(0)

print(ans)