arr = list(map(int, input().split()))

n = len(arr)
arr.sort()
cnt = 0

for i in range(n-1):
    cnt += arr[i]*(n-i-1)
print(cnt)