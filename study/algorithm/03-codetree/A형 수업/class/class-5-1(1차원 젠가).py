n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
s1, e1, s2, e2 = s1 - 1, e1 -1, s2 - 1, e2 - 1
points = [(s1, e1), (s2, e2)]

cnt = 0
while cnt < 2:

    temp = []
    s, e = points[cnt]

    for i in range(len(blocks)):
        if i not in range(s, e+1):
            temp.append(blocks[i])

    blocks = temp
    cnt += 1

print(len(blocks))
print(*blocks, sep = '\n')