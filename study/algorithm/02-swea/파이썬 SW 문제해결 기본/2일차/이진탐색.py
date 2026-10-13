T = int(input())
for test_case in range(1,T+1):
  P, Pa, Pb = map(int, input().split())
  def binary_count(P, target):
    left = 1
    right = P
    cnt = 0
    while True :
      mid = int((left+right)/2)
      cnt +=1

      if mid == target:
        return cnt
      elif target < mid:
        right = mid
      else :
        left = mid

  a = binary_count(P, Pa)
  b = binary_count(P, Pb)
  if a > b:
    print(f"#{test_case} B")
  elif a < b:
    print(f"#{test_case} A")
  else:
    print(f"#{test_case} 0")