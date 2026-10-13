T = int(input())

for tc in range(1, T + 1):
    # n 배열 크기, m 맨앞 숫자 맨뒤로 보내는 작업 수
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    for _ in range(m):
        temp = arr.pop(0)
        arr.append(temp)

    print(f'#{tc}', arr[0])