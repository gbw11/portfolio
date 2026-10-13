T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    max_value = -1

    for i in range(n):
        cnt = 1
        for j in range(i+1, n):
            if abs(arr[i]-arr[j]) <= k:
                cnt += 1

        max_value = max(max_value, cnt)

    print(f'#{tc} {max_value}')