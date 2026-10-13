n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# m개뽑은 점들 중에서 가장 먼 두 점 사이의 거리를 리턴하는 함수
def get_max_dist():
    dist = float('-inf')
    for i in range(len(path)):
        x1, y1 = path[i]
        for j in range(i + 1, len(path)):
            x2, y2 = path[j]
            dist = max(dist, (x1 - x2)**2 + (y1 - y2)**2)
    return dist


path = []
result = float('inf')
def dfs(lev, start):
    global result

    if lev == m:
        # 가장 먼 거리들 중에서 최솟값을 찾는 중
        dist = get_max_dist()
        result = min(result, dist)
        return

    # 반복문 돌면서 좌표를 찾아서 넣고
    for i in range(start, n):
        path.append(points[i])
        # 중복허락하지 않는 조합이기 때문에
        # start 매개변수 만들어서 실행시키기
        dfs(lev + 1, i + 1)
        path.pop()


dfs(0, 0)
print(result)