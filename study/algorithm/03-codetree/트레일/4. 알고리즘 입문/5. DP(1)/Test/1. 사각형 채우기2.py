n = int(input())

# Please write your code here.

def fibbo(n):
    if n == 1:
        return 1

    dp = [0]*(n+1)

    dp[1] = 1
    dp[2] = 3


    for i in range(3, n+1):
        # 2배 하는 이유는 2칸 남았을 때 ㅣㅣ 넣는 경우는 dp[i-1]에서 이미 처리한 거기 때문
        dp[i] = dp[i-1] + dp[i-2]*2

    return dp[n]

print(fibbo(n) % 10007)