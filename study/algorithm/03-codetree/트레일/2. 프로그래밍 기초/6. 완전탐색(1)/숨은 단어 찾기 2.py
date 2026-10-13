N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)] # 각각의 문자를 리스트이 원소

# Please write your code here.

#상하좌우 + 대각선까지 체크
dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

cnt = 0

for y in range(N):
    for x in range(M):
        if arr[y][x] == 'L':
            for i in range(8):
                for k in range(1,3):
                    ny = y + dy[i]*k
                    nx = x + dx[i]*k
                    if not(0 <= ny < N and 0 <= nx < M):
                        break
                    if arr[ny][nx] != "E":
                        break
                else: cnt += 1

print(cnt)
