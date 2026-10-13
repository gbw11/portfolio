T =  int(input())
for test_case in range(1, T+1):
  N = int(input())
  arr = list(map(int, input().split()))
  arr.sort()

  first = 0
  last = N-1
  numbers = []
  while first <= last:
    numbers.append(arr[last])
    numbers.append(arr[first])
    first +=1
    last -=1
  result = numbers[:10]

  print(f"#{test_case}", *result)