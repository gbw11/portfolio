n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def finding(i, j):
    cnt = 0
    for y in range(3):
        for x in range(3):
            if grid[i+y][j+x]==1:
                cnt +=1
    return cnt

result = 0
for i in range(n-2):
    for j in range(n-2):
        coin = finding(i, j)
        result = max(coin, result)

print(result)