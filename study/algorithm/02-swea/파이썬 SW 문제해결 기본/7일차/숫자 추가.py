t = int(input())

for tc in range(1, t+1):
    n, m, l = map(int, input().split())

    arr = list(map(int, input().split()))

    for _ in range(m):
        idx, num = map(int, input().split())
        arr.insert(idx, num)

    print(f'#{tc}', arr[l])