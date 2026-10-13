n, m = map(int, input().split()) # 행과 열
k = int(input()) # 폭탄의 화력
arr = [list(input()) for _ in range(n)]

#  #:벽, @:폭탄, _:빈칸

#상하좌우and 대각선까지 만들기
A, B = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]
#상하좌우
dy, dx = A[::2], B[::2]
#대각선
dcy, dcx = A[1::2], B[1::2]

def in_range(y,x):
    return 0<=y<n and 0<=x<m

for y in range(n):
    for x in range(m):
        if arr[y][x]=='@':
            arr[y][x] = '%'
            for l in range(4): # 상하좌우 탐색
                for a in range(1,k+1):
                    ny = y + dy[l]*a
                    nx = x + dx[l]*a
                
                    if in_range(ny,nx) and arr[ny][nx]=='_':
                        arr[ny][nx] = '%'

            for l in range(4): # 대각선 탐색
                for b in range(1,k+1):
                    ny = y + dcy[l]*b
                    nx = x + dcx[l]*b
                    
                    if not in_range(ny,nx):
                        break

                    if arr[y][nx]=='#' or arr[ny][x]=='#':
                        break

                    if arr[ny][nx] == '_':
                        arr[ny][nx] = '%'

                    
print(arr)
