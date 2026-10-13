n = int(input())

# Please write your code here.

coins = [1, 2, 5]

dp = [0] * (n + 1)
dp[0] = 1  # 아무것도 안 고르는 경우 1가지

for j in range(1, n + 1):      # 합 기준으로 바깥 루프
    for coin in coins:          # 매 합마다 1, 2, 5 전부 시도
        if j - coin >= 0:
            dp[j] += dp[j - coin]
    # 결과 낼 때 너무 큰 수여서 10007로 나눈 나머지 출력하라고 문제에서 제시했기 때문
    # 근데 MOD 연산의 특징 때문에 제일 마지막이 아닌 중간에 계속해도 상관이 없음!
    dp[n] %= 10007

print(dp[n])