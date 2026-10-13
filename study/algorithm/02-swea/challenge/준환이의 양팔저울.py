from math import factorial

def recur(depth, lsum, rsum, remain):
    global cnt

    if rsum > lsum:
        return

    if lsum >= rsum + remain:
        k = n - depth
        cnt += (2**k) * factorial(k)
        return

    if depth == n:
        cnt += 1
        return

    prev = -1
    for i in range(n):
        if not used[i]:
            if arr[i] == prev:
                continue
            prev = arr[i]

            used[i] = True
            recur(depth+1, lsum + arr[i], rsum, remain - arr[i])   # 왼쪽
            if lsum >= rsum + arr[i]:
                recur(depth+1, lsum, rsum + arr[i], remain - arr[i])   # 오른쪽
            used[i] = False

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    used = [False] * n
    cnt = 0
    recur(0, 0, 0, sum(arr))
    print(f'#{tc}', cnt)