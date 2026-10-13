arr = [0, 9, 4, 12, 3, 6, 0, 15, 0, 0, 0, 0, 0, 0, 13, 17]
arr = arr + [0] * 100

result = []

def dfs(now):
    if arr[now] == 0:
        return

    result.append(arr[now])
    dfs(now * 2)
    dfs(now*2 + 1)

dfs(1)
print(*result)