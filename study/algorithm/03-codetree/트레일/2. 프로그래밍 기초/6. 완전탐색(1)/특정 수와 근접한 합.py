N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

result = S
new_arr = arr[:]

for i in range(N-1):
    for j in range(i+1, N):
        new_arr.pop(i,j)

        result = min(result, sum(new_arr)-S)
        new_arr = arr[:]

print(result)