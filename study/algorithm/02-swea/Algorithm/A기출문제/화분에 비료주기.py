def recur(lev):
    global res
    if lev==n:
        ans = 0
        for i, num in enumerate(path):
            if i <= n-2:
                if path[i] == path[i+1]:
                    ans -= p
            if num==0:
               ans += A[i]
            else:
                ans += B[i]
        res = max(res, ans)
        return

    for i in range(2):
        path.append(i)
        recur(lev+1)
        path.pop()



t = int(input())
for tc in range(1, t+1):
    # n : 화분의 수, p : 줄어드는 비료의 양
    n, p = map(int, input().split())
    # A : a비료 자라나는 식물의 크기,  B: b 비료 자라나는 식물의 크기
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    path = []
    res = 0
    recur(0)
    print(f'#{tc}', res)