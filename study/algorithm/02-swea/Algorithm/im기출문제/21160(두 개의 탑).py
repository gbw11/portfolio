T = int(input())

for tc in range(1, T + 1):

    n, m1, m2 = map(int, input().split())

    arr = list(map(int, input().split()))

    arr.sort(reverse=False)
    cnt = 0
    for i in range(1, max(m1, m2)+1):
        if i <= m1:
            cnt += i*arr.pop()

        if i <= m2:
            cnt += i*arr.pop()
    print(f'#{tc}', cnt)