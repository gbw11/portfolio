T = int(input())

for tc in range(1, T + 1):

    n = int(input())

    arr = [0 for _ in range(n+1)]

    target = [0] + list(map(int, input().split()))

    def turn(i):
        if arr[i] == 1:
            arr[i] = 0
        else:
            arr[i] = 1

    cnt = 0
    for idx in range(1, n + 1):
        if arr[idx] != target[idx]:
            for i in range(idx, n + 1):
                if i % idx == 0:
                    turn(i)

            cnt += 1

    print(f'#{tc}', cnt)

