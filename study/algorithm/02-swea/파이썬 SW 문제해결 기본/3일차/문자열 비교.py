T = int(input())
for test_case in range(1, T+1):
  str1 = input()
  str2 = input()
  N, M = len(str1), len(str2)
  equal = False
  for i in range(M):
    if str1 == str2[i:i+N]:
      print(f"#{test_case} 1")
      equal = True
      break

  else:
    print(f"#{test_case} 0")