T = int(input())
for test_case in range(1, T+1):
    N = int(input())  #방 가로 길이
    arr = list(map(int, input().split()))

    cnt_arr =[]
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if arr[i]>arr[j]:
                cnt += 1

        cnt_arr.append(cnt)

    print(f"#{test_case} {max(cnt_arr)}")