n = int(input())

arr = list(map(int, input().split()))

arr.sort(reverse = True)


cnt = 0
val = 0
while arr:
    val += arr.pop()
    if val >100:
        break

    cnt += 1

print(cnt)