n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

cnt = 0
for i in range(n):
    if arr[i]>t :
        k = 1
        for j in range(i+1, n):
            if arr[j]>t:
                k += 1
            else: break
        cnt = max(cnt, k)

print(cnt)