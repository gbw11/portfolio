T = int(input())

for tc in range(1, T+1):
    n = int(input())
    trees = list(map(int, input().split()))

    target = max(trees)

    one = 0
    two = 0

    for t in trees:
        diff = target - t
        two += diff // 2
        one += diff % 2

    if one > two:
        ans = one * 2 - 1
    else:
        remain = two - one
        ans = one * 2
        ans += (remain // 3) * 4

        if remain % 3 == 1:
            ans += 2
        elif remain % 3 == 2:
            ans += 3

    print(f'#{tc}', ans)