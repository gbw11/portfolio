n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

arr.sort()

result = max(arr[0]*arr[1]*arr[-1], arr[-1]*arr[-2]*arr[-3])

print(result)