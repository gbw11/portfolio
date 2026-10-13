t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    arr = []
    for _ in range(m):
        tmp = list(map(int, input().split()))

        k = len(arr)
        if not arr:
            arr = tmp

        else:
            for i in range(len(arr)):
                if arr[i] > tmp[0]:
                    # arr의 i번째 위치에 tmp를 삽입하는방법
                    # 슬라이싱보다 시간이 훨씬 줄어든다.
                    arr[i:i] =tmp
                    break
        if k == len(arr):
            arr.extend(tmp)

    ans = arr[-1:-11:-1]
    print(f'#{tc}', *ans)