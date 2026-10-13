T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 게임판 안의 숫자들 찾기위한 판
    # sum(arr,[]) = [] + arr[0] + arr[1] + ...
    numbers = set(sum(arr,[]))

    squares=[]

    for num in numbers:
        board=[]         #각 숫자의 위치를 저장하기위한 리스트
        for i in range(n):
            for j in range(n):
                if arr[i][j] == num:
                    board.append((i,j))

        if not board:
            continue

        for ch1 in board:
            for ch2 in board:
                y1, x1 = ch1[0], ch1[1]
                y2, x2 = ch2[0], ch2[1]
                square = (y1-y2+1)*(x1-x2+1)
                if square > 1:
                    squares.append(square)

    result = squares.count(max(squares))
    print(f"#{test_case} {result}")

