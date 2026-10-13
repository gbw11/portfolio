t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    # m번째 칸에 추가, k번 반복
    arr = list(map(int, input().split()))

    idx = 0
    for _ in range(k):
        idx = (idx + m) % len(arr)

        if idx == 0:
            new_num = arr[-1] + arr[0]

        else:
            new_num = arr[idx - 1] + arr[idx]
        arr.insert(idx, new_num)

    print(f'#{tc}', *arr[-1:-11:-1])

