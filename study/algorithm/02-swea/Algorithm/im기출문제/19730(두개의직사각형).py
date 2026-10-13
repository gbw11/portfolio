T = int(input())

for tc in range(1, T+1):
    y1, x1, y2, x2 = map(int, input().split())
    i1, j1, i2, j2 = map(int, input().split())

    board = [[0]*1000 for _ in range(1000)]

    result = 0 # 결과값 저장

    # 3 번 상황(모서리에서 만날때)
    if (y1==i2 and x1==j2) or (y1==i2 and x2==j1) or (y2==i1 and x1==j2) or (y2==i1 and x2==j1):
        result = 3

    # 2 번 상황(겹치는 선 존재)
    elif i1==y2 or i2==y1 or x1==j2 or x2==j1:
        result = 2

    # 1번 상황
    else:
        for y in range(y1, y2):
            for x in range(x1, x2):
                board[y][x] =1

        valid = False
        for i in range(i1, i2):
            for j in range(j1, j2):
                if board[i][j] == 1:
                    result = 1
                    valid = True
                    break
            if valid:
                break
    # 4번 상황
    if result == 0: # 1,2,3에서 결과 안바꼈으면
        result = 4

    print(f'#{tc}', result)