n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


# Please write your code here.



# 폭탄 터트린 결과 저장 temp
def boom(y, x):
    # 임시 배열 생성
    temp = [rows[:] for rows in grid]
    power = temp[y][x]
    temp[y][x] = 0
    dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
    for dy, dx in zip(dys, dxs):  # 상하좌우 돌리고
        for k in range(1, power):  # 상하좌우 길이만큼 검
            ny = y + dy * k
            nx = x + dx * k

            if not (0 <= ny < n and 0 <= nx < n): continue
            temp[ny][nx] = 0

    return temp


# 실행 끝냈을 때 인접한 격자 체크하기
# 오른쪽이랑 아래만 체크하면됌!
drs, dcs = [0, 1], [1, 0]

result = 0
for y in range(n):
    for x in range(n):
        # temp 배열에 폭탄 터진 후 배열 저장
        temp = boom(y, x)

        # 중력작용 하는 거 기록
        for j in range(n):
            temp_col = []
            for i in range(n):
                if temp[i][j] != 0:
                    temp_col.append(temp[i][j])

            temp_col = [0] * (n - len(temp_col)) + temp_col[:]

            for p in range(n):
                temp[p][j] = temp_col[p]
            # 중력 작용 완료

        # 완료된 배열에서 조건 만족하는 쌍 찾기
        cnt = 0
        for r in range(n):
            for c in range(n):
                for dr, dc in zip(drs, dcs):
                    nr = r + dr
                    nc = c + dc
                    if not (0 <= nr < n and 0 <= nc < n): continue

                    # 0이 아닌 애들 중에서 같은 거 체크해야함 0은 터지고 없는 거기때문에!!
                    if temp[r][c] != 0 and temp[r][c] == temp[nr][nc]:
                        cnt += 1
        result = max(result, cnt)

print(result)

# 반복물 돌때 temp = boom(y,x) 형태로 진행할 것