n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Please write your code here.

for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j and (x2[i] < x1[j] or x1[i] > x2[j]):
            continue

        cnt += 1

    if cnt == n:
        print('Yes')
        break

else:
    print('No')