# 4835
T = int(input())
for test_case in range(1,T+1):
  N, M = map(int, input().split())
  num = list(map(int, input().split()))

  max_sum = float("-inf")
  for i in range(len(num)+1-M):

    if sum(num[i:i+M])>max_sum:
      max_sum = sum(num[i:i+M])

  min_sum = float("inf")
  for i in range(len(num)+1-M):

    if sum(num[i:i+M])<min_sum:
      min_sum = sum(num[i:i+M])


  result = max_sum-min_sum

  print(f"#{test_case} {result}")