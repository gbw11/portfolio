T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = list(map(int, input().split()))
    max_height = max(tree)
    day = 0
    extra = []
    cnt_1 = 0
    cnt_2 = 0
    for i in range(N):
        remain = max_height - tree[i]
        cnt_2 += (remain // 2)
        cnt_1 += (remain % 2)
        # day += (remain // 3) * 2
        # extra.append(remain % 3)

    # cnt_1 = extra.count(1)
    # cnt_2 = extra.count(2)
    min_cnt = min(cnt_1, cnt_2)
    day += (min_cnt * 2)
    cnt_1 -= min_cnt
    cnt_2 -= min_cnt
    if cnt_1 > cnt_2:
        day += (cnt_1 * 2 - 1)
    else:
        while cnt_2 - cnt_1 >= 2:
            cnt_1 += 2
            cnt_2 -= 1
        if cnt_1 > cnt_2:
            day += (cnt_2 * 2) + 1
        elif cnt_1 == cnt_2:
            day += (cnt_1 * 2)
        else:
            day += (cnt_2 * 2)

    print(f'#{tc} {day}')