# 4836
T = int(input())
for test_case in range(1, T+1):
  paper = [[0]*10 for _ in range(10)]
  N = int(input())
  for _ in range(N):
    r1, c1, r2, c2, col = map(int, input().split())
    for r in range(r1,r2+1):
      for c in range(c1, c2+1):
        if paper[r][c] == 0:
          paper[r][c] = col
        elif paper[r][c] == col:
          pass
        else:
          paper[r][c] = 3

  target = 3
  cnt = sum(row.count(target) for row in paper)
  print(f"#{test_case} {cnt}")