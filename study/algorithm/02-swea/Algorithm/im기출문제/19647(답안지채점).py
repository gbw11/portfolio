T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split()) # n : 학생,  m : 문제 수

    solution = list(map(int, input().split()))

    students = [list(map(int, input().split())) for _ in range(n)]

    result1 = float('-inf')
    result2 = float('inf')
    for student in students:
        stack = []
        for i in range(m):
            if student[i] == solution[i]:
                if not stack:
                    stack.append(1)
                else:
                    stack.append(stack[-1]+1)
            else:
                stack.append(0)

        result1 = max(result1, sum(stack))
        result2 = min(result2, sum(stack))

    result = result1-result2
    print(f'#{tc}', result)
