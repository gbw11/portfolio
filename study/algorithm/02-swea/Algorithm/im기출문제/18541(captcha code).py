T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())  # 샘플 길이, 패스코드 길이
    sample = ''.join(input().split())
    passcode = ''.join(input().split())


    temp = -1
    cnt = 0

    for i in range(k):
        temp = sample.find(passcode[i], temp+1)
        if temp == -1:  # 못찾으면 -1 반환
            break
        cnt += 1

    if cnt == k:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')