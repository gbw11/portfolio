t = int(input())
def recur(lev, start):
    if lev == n//2:
        b_arr = list(set(arr) - set(path))
        sum_v1 = 0
        sum_v2 = 0
        for i1, i2 in zip(b_arr, path):
            for j1, j2 in zip(b_arr, path):
              sum_v1 += grid[i1][j1]
              sum_v2 += grid[i2][j2]
        result.append(abs(sum_v1 - sum_v2))
        return

    for i in range(start, n):
        path.append(i)
        recur(lev+1, i+1)
        path.pop()



for tc in range(1, t+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    path = []
    arr = [i for i in range(n)]
    result = []
    recur(0, 0)
    result.sort()
    print(f'#{tc}', result[0])