n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


result = 0

for y in range(n-2):
    for x in range(n-2):
        cnt = sum(sum(rows[x:x+3]) for rows in grid[y:y+3])
        result = max(result, cnt)

print(result)