T =  int(input())

for test_case in range(1,T+1):
  lst = []
  text = input()
  valid = True

  for ch in text:
    if ch in "({":
      lst.append(ch)

    elif ch ==  ")":
      if not lst or lst[-1] != "(":
        valid = False
        break
      lst.pop()

    elif ch ==  "}":
      if not lst or lst[-1] != "{":
        valid = False
        break
      lst.pop()


  if lst :
    valid = False

  print(f"#{test_case} {1 if valid else 0}")