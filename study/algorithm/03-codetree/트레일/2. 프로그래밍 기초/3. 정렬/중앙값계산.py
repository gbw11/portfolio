n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

result = []
for i in range(n):
    if i % 2 == 0:
        sub = arr[:i+1]
        result.append(sorted(sub)[len(sub)//2])

print(*result)