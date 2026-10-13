import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

t = int(input())

for tc in range(1, t+1):
    day, month, three, year = map(int, input().split())

    plan = list(map(int, input().split()))

    dp = [float('inf')] *13
    dp[0] = 0

    for i in range(1, 13):
        #1일권
        dp[i] = min(dp[i], dp[i-1]+ day*plan[i-1])
        #1달권
        dp[i] = min(dp[i], dp[i-1]+ month)
        #3달권
        dp[i] = min(dp[i], dp[max(0, i-3)]+three)
        #1년권
        dp[12] = min(dp[12], year)

    print(f'#{tc}', dp[12])