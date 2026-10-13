n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.

lines = []

for p, q in zip(x1, x2):
    lines.append((p, q))

lines.sort(key = lambda x : x[1])


count = 0
last_end = float('-inf')

for start, end in lines:
    if start > last_end:
        count += 1
        last_end = end

print(count)