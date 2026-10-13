T = int(input())
for test_case in range(1,T+1):
  N , M = map(int, input().split())
  arr = [list(input()) for _ in range(N)]

  # 가로 회문 찾기

  found = False

  for i in range(N):
    for j in range(N-M+1):
      word = arr[i][j:j+M]
      if word == word [::-1]:
        print(f"#{test_case}", "".join(word))
        found = True
        break
    if found:
      break

  # 세로 회문 찾기
  if not found :
    for i in range(N):
      for j in range(N-M+1):
        word = [arr[j+k][i] for k in range(M)]
        if word == word[::-1]:
          print(f"#{test_case}", "".join(word))
          found = True
          break

      if found :
        break
