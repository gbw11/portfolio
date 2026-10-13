X, Y = map(int, input().split())

# Please write your code here.

cnt = 0
for num in range(X, Y+1):
    arr = [ch for ch in str(num)]
    if arr == arr[::-1]:
        cnt += 1

print(cnt)