T = int(input())
for test_case in range(1, T+1):
  num = int(input())
  n = num//10
  dp = [0]*(n+1)
  dp[0] = 1
  dp[1] = 1
  for i in range(2, n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]
  
  print(f"#{test_case} {dp[n]}")