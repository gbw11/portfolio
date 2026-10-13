T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]

    # 가로줄에서 찾기
    def row_find():
        for y in range(n):
            arr = board[y]
            for x in range(n-m+1):
                if arr[x:x+m] == arr[x:x+m][::-1]:
                    return arr[x:x+m]
        return None

    # 세로줄에서 찾기
    def col_find():
        for x in range(n):
            for y in range(n-m+1):
                arr = []
                for i in range(m):
                    arr.append(board[y+i][x])
                if arr == arr[::-1]:
                    return arr
        return None

    res = row_find()
    if res:
        print(f'#{tc}', ''.join(res))
    else:
        res = col_find()
        print(f'#{tc}', ''.join(res))
