T = int(input())

for tc in range(1, T+1):

    # n은 배열 크기, k는 글자의 길이
    n, k = map(int, input().split())

    # 흰색은 1, 검정은 0
    board = [list(map(int, input().split())) for _ in range(n)]

    # 상하좌우 탐색
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    cnt = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == 1:
                for i in range(4):
                    for p in range(1, k):
                        ny = y + dy[i]*p
                        nx = x + dx[i]*p
                        if not(0 <= ny < n and 0 <= nx < n):
                            break
                        if board[ny][nx] == 0:
                            break
                    else:
                        # 시작 점의 앞의 부분
                        ny1 = y + dy[(i+2) % 4]
                        nx1 = x + dx[(i+2) % 4]

                        # 마지막 글자의 다음 부분
                        ny2 = y+dy[i]*k
                        nx2 = x+dx[i]*k

                        # 글자의 앞뒤가 범위를 벗어나거나 0일 경우를 체크한 다음 +1
                        # 만약 3개를 찾는데 칸이 4개인 경우를 세지 않기 위한 과정
                        if not(0 <= ny2 < n and 0 <= nx2 < n) or board[ny2][nx2] == 0:
                            if not(0 <= ny1 < n and 0 <= nx1 < n) or board[ny1][nx1] == 0:
                                cnt += 1

    # 상하좌우 탐색하면 똑같은거 2번씩 세니깐 마지막에 2로 나눈다
    print(f'#{tc}', cnt//2)