t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input().split()))

    cnt = 0

    for i in range(2,0,-1):
        if arr[i-1]>=arr[i]:
            val = arr[i-1]-arr[i] +1
            cnt += val
            arr[i-1] -= val

    for a in arr:
        if a < 1:
            print(f'#{tc}',-1)
            break
    else: print(f'#{tc}', cnt)