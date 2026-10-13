T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    if (m & ((1 << n) - 1)) == ((1 << n) - 1):
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')