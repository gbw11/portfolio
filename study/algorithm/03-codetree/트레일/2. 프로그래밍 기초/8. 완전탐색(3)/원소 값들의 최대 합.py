n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.

result = 0

for i in range(1, n + 1):

    cnt = 0  # 숫자합 저장
    j = i
    but = 0  # 종료 조건
    while True:
        if but == m:
            break
        cnt += arr[j]
        j = arr[j]
        but += 1

    result = max(result, cnt)

print(result)
