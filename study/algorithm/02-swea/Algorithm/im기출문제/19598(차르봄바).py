T = int(input())

for test_case in range(1, T+1):
    N, P = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))


    max_result = 0

    for r in range(N):
        for c in range(N):
            result = 0

            left = max(0, c - P)
            right = min(N - 1, c + P)
            up = max(0, r - P)
            down = min(N - 1, r + P)


            for i in range(left, right+1):
                result += arr[r][i]

            for j in range(up, down+1):
                result += arr[j][c]

            result -= arr[r][c]

            max_result = max(max_result, result)

    print(f"#{test_case} {max_result}")


