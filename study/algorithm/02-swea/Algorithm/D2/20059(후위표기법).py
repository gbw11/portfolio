T = int(input())

for tc in range(1, T+1):
    text = input().split()

    stack = []
    valid = True
    for ch in text:
        if ch =='.': break

        elif ch.isdigit():
            stack.append(int(ch))

        else:
            if len(stack)<2:
                valid = False
                break

            b = stack.pop()
            a = stack.pop()
            if ch =='+': stack.append(a + b)
            elif ch =='-': stack.append(a - b)
            elif ch =='*': stack.append(a * b)
            elif ch =='/': stack.append(a // b) # 나눗셈 연산 사용시 결과값 float

    if valid and len(stack) == 1:
        print(f'#{tc}', stack.pop())
    else:
        print(f'#{tc}', 'error')