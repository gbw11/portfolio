T = int(input())
for test_case in range(1,T+1):

    arr = input().split()
    stack = []
    error = False
    
    for ch in arr:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            if ch == '.':
                break
            if len(stack)<2:
                error = True
                break
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a+b)
            
            elif ch == '-':
                stack.append(a-b)
            elif ch == '*':
                stack.append(a*b)
            elif ch == '/':
                stack.append(a//b)

    if error or len(stack) !=1:
        print(f'#{test_case} error')
    else:
        print(f'#{test_case} {stack[0]}')
