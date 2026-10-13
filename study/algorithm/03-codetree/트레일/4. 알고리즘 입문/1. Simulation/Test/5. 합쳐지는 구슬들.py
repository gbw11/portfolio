n, m, t = map(int, input().split()) # n:행,열  m 구슬의 수, t 시간

r = [] # 행
c = [] # 열
d = [] # 방향 UDRL
w = [] # 무게 

for _ in range(m):
    ri, ci, di, wi = input().split()
    r.append(int(ri) - 1)
    c.append(int(ci) - 1)
    d.append(di)
    w.append(int(wi))

# Please write your code here.

# d 방향 배열 U R D L => 0 1 2 3 으로 변환하기
mapper = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3
}
# 방향을 숫자로 변환
for i in range(len(d)):
    d[i] = mapper[d[i]] 


board = [[0] * n for _ in range(n)]

# 판에 (w, d) = (무게, 방향, 순서) 기록
for i in range(m):
    board[r[i]][c[i]] = (w[i], d[i], i+1)


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

#다음 상황을 기록하는 함수
def change():
    dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
    temp = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            p = board[y][x]  #  p = (무게, 방향, 순서)
            if p != 0:
                ny = y + dys[p[1]]
                nx = x + dxs[p[1]]
                # 벽과 충돌했다면 
                if not in_range(ny,nx):
                    # 원래 위치에 다른 애가 들어있는 경우를 처리해야함!!
                    # 위치는 그대로에 방향정보만 바꿔서 기록
                    if temp[y][x] == 0:
                        temp[y][x] = (p[0], (p[1] + 2) % 4, p[2])

                    # 위치에 다른게 들어있는 경우 충돌 처리 해줘야함
                    else: # 기존게 이길경우 무게만 더한 뒤 입력
                        if temp[y][x][2] > p[2]:
                            temp[y][x] = (p[0]+ temp[y][x][0], temp[y][x][1], temp[y][x][2])
                        # 새로 들어오는게 이길경우 방향을 바꿔서 입력
                        else:
                            temp[y][x] = (p[0]+ temp[y][x][0], (p[1] + 2) % 4, p[2])
                # 다음 위치에 저장할 때 / 다음 위치가 비어있는지, 다른게 들어있는지 체크 필요
                # 다음 위치가 비었다면
                elif temp[ny][nx] == 0:
                    temp[ny][nx] = p
                # 충돌이 발생한다면
                else:
                    if temp[ny][nx][2] > p[2]:
                        temp[ny][nx] = (p[0]+ temp[ny][nx][0], temp[ny][nx][1], temp[ny][nx][2])
                    else:
                        temp[ny][nx] = (p[0]+ temp[ny][nx][0], p[1], p[2])
    # 진행 완료된 결과를 돌려준다.
    return temp

for _ in range(t):
    temp = change()
    board = [rows[:] for rows in temp]

cnt = 0
max_v = 0
for y in range(n):
    for x in range(n):
        if board[y][x] != 0:
            cnt +=1
            max_v = max(max_v, board[y][x][0])

print(cnt, max_v)