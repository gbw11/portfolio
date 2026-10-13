n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

result = 0
for i in range(n-k+1):
    result = max(result, sum(arr[i:i+k]))

print(result)