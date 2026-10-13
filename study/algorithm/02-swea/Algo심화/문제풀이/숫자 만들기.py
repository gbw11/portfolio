# 사칙 연산의 횟수가 정해져있다.
# 특정 시점에 연산자가 남아있는지 보아야 한다.
# 완전탐색으로 진행시 11! =4000만번 이어서 터짐?
# no! 사칙연산이기 때문에 4^11

import sys
sys.stdin = open("input.txt", "r")

# 종료조건: 첫번째 숫자부터 시작, 숫자를 모두 고려하면 종료
# 가지의 수 : 최대 4개(사칙연산)
# 누적값 (현재 시점의 값과 다음 시점의 값은 무엇이어야 하는가?)
#   - 남은 연산자의 수

def recur(cnt, total, plus, minus, mul, div):
    global min_result, max_result

    if cnt == n:
        # 최대, 최소 계산
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return

    # 덧셈
    if plus > 0:
        recur(cnt+1, total + numbers[cnt], plus-1, minus, mul, div)
    # 뺄셈
    if minus > 0:
        recur(cnt+1, total - numbers[cnt], plus, minus-1, mul, div)
    # 곱셈
    if mul > 0:
        recur(cnt+1, total * numbers[cnt], plus, minus, mul-1, div)
    # 나눗셈
    if div > 0:
        recur(cnt+1, int(total / numbers[cnt]), plus, minus, mul, div-1)

t = int(input())
for tc in range(1, t+1):
    n = int(input())

    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_result, max_result = 1e10, -1e10

    recur(1, numbers[0], opers[0], opers[1], opers[2], opers[3])
    print(f"#{tc}", max_result-min_result)