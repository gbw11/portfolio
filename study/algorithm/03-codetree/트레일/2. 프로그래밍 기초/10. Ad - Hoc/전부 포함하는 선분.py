n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.


result = 101

for i in range(n):
    counts = [0 for _ in range(101)]
    for j in range(n):
        if i != j:
            x = segments[j][0]
            y = segments[j][1]

            for k in range(x, y + 1):
                counts[k] = 1

    left = 0
    right = 101
    for a in range(101):
        if counts[a] == 1:
            left = a
            break
    for b in range(100, 0, -1):
        if counts[b] == 1:
            right = b
            break

    result = min(result, right - left)

print(result)