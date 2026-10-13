n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.

coins.sort(reverse=True)
cnt = 0
while k > 0:
    for coin in coins:
        if k >= coin:
            k -= coin
            cnt +=1
            break

print(cnt)

## 해설 코드
'''
for coin in coins[::-1]:
    ans += k // coin
    k %= coin
''' 