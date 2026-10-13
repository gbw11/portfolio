n = int(input())


result = []
def recur(idx = 0):
    if idx == n:
        print(*result)
        return

    for i in range(1, 7):
        result.append(i)
        recur(idx+1)
        result.pop()

    return

recur()