n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda x : (x[1], x[0]))

cnt = 0
curr_end = 0

for s, e in arr:
    if s >= curr_end:
        cnt +=1
        curr_end = e
print(cnt)

