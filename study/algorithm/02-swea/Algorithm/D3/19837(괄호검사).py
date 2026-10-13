T = int(input())

for tc in range(1, T+1):

    stack = []
    text = input()
    valid = True

    for ch in text:
        if ch == '(' or ch == '{':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack.pop() != '(':
                valid = False
                break

        elif ch == '}':
            if not stack or stack.pop() != '{':
                valid = False
                break
    if stack:
        valid = False

    print(f'#{tc}', 1 if valid else 0)