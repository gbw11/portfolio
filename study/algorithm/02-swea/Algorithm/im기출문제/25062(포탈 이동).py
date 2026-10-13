t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    point = 1
    cnt = 0
    while True:
        
        if arr[point] != 0:
            arr[point], point = 0, arr[point]
            if point > n:
                break
            cnt += 1
            
        else:
            point += 1
            if point > n:
                break
            cnt += 1

    print(f'#{tc}', cnt)