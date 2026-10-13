# 숫자카드 4834
T = int(input())
for test_case in range(1, T+1):
  N = int(input())
  num = input().strip()
  count = [0] * 10
  for ch in num:
    count[int(ch)] += 1

  count.reverse()
  max_cnt = max(count)
  most_num = 9 -  count.index(max_cnt)

  print(f"#{test_case} {most_num} {max_cnt}")