x, y= 2, 4
dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

# 범위를 벗어났는지 여부를 판단하는 함수
def in_range(y,x):
    return 0<=y<5 and 0<=x<5 # 배열 크기에 따라서 변한다.


cnt = 0
# 상하좌우 탐색
for i in range(4):
    ny = y + dys[i]
    nx = x + dxs[i]

    # 행렬 벗어나면 정지
    # if not in_range(ny, nx):
        # return
    
## ==============w 정답 코드=====

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]


def in_range(y,x):
    return 0<=x and x<n and 0<=y and y<n

result = 0

for y in range(n):
    for x in range(n):
        # (y, x)에 대해서

        cnt = 0

        # 상하좌우를 탐색하면서
        for i in range(4):
            ny = y + dys[i]
            nx = x + dxs[i]

            if not in_range(ny, nx):
                continue
            
            # 1의 갯수를 세는거기 때문에 비어있으면 0이고
            cnt += grid[ny][nx]
        
        if cnt>=3:
            result +=1
print(result)