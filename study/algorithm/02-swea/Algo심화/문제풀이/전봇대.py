t = int(input())

for tc in range(1, t+1):
    n = int(input())

    arr = [tuple(map(int, input().split())) for _ in range(n)]

    arr.sort()

    b = [x[1] for x in arr]

    cnt = 0

    for i in range(n):
        for j in range(i+1, n):
            if b[i] > b[j]:
                cnt += 1

    print(f'#{tc}', cnt)