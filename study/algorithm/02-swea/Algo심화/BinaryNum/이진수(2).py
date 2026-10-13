T = int(input())

for tc in range(1, T+1):
    N = float(input())

    res = ""
    cnt = 0

    while N > 0:
        N *= 2

        if N >= 1:
            res += '1'
            N -= 1
        else:
            res += '0'

        cnt += 1

        if cnt > 12:
            res = "overflow"
            break

    print(f'#{tc} {res}')