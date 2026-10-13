n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


path = []
used = [0] * (n + 1)
result = 0
def dfs(lev):
    global result
    if lev == n:
        temp = []
        for i in range(n):
            temp.append(grid[i][path[i]])
        result = max(result, min(temp))

        return

    for i in range(n):
        if used[i] == 1 : continue
        used[i] = 1
        path.append(i)
    
        dfs(lev + 1)
        path.pop()
        used[i] = 0


dfs(0)
print(result)