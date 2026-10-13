T = int(input())
for test_case in range(1, T+1):
  str1 = input()
  str2 = input()

  lst = []
  for ch in str1 :
    cnt = 0
    for j in str2 :
      if ch == j:
        cnt +=1
    lst.append(cnt)

  print(f"#{test_case} {max(lst)}")