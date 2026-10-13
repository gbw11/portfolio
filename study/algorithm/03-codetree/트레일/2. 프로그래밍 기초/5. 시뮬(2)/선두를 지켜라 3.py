N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

a = [0]
b = [0]
# a의 위치 기록   # [0, 1, 2, 6, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
for i in range(N):
    for _ in range(t[i]):
        a.append(a[-1] + v[i])
# b의 위치 기록  # [0, 2, 4, 6, 7, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
for i in range(M):
    for _ in range(t2[i]):
        b.append(b[-1] + v2[i])

cnt = 0

for i in range(len(a) - 1):
    if a[i] < b[i] and a[i + 1] >= b[i + 1]:
        cnt += 1

    elif a[i] <= b[i] and a[i + 1] > b[i + 1]:
        cnt += 1

    elif a[i] > b[i] and a[i + 1] <= b[i + 1]:
        cnt += 1

    elif a[i] >= b[i] and a[i + 1] < b[i + 1]:
        cnt += 1

print(cnt)