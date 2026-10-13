T = int(input())
for test_case in range(1, T+1):
  text = input()
  stack = []

  for ch in text:
    if stack and stack[-1] == ch:
      stack.pop()
    else:
      stack.append(ch)

  print(f"#{test_case} {len(stack)}")
