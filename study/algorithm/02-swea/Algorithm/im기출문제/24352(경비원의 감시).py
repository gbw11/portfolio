def in_range(y,x):
    return 0<=x<n and 0<=y<n

def monitor(y,x):
    cnt = 0
    for i in range(4):
        for k in range(1,n):
            ny = y + dy[i]*k
            nx = x + dx[i]*k
            if not in_range(ny,nx): break
            else:
                if arr[ny][nx]==1:
                    break
                elif arr[ny][nx]==0:
                    cnt +=1

    return cnt
#======= 위는 함수 정의 파트 ==============
T = int(input())
for tc in range(1, T+1):


    n = int(input())
    arr = [list(map(int, input().split())) for _  in range(n)]

    dy, dx = [-1, 0 ,1, 0 ], [0, 1, 0, -1]

    valid = False
    for y in range(n):
        for x in range(n):
            if arr[y][x] == 2:
                see = monitor(y,x)
                valid = True
                break
        if valid:
            break
    block = 0
    for y in range(n):
        for x in range(n):
            if arr[y][x] == 1:
                block +=1
    result = n**2 - (block +see +1)
    print(f'#{tc} {result}')