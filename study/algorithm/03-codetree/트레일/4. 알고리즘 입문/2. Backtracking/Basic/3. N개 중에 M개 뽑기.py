n, m = map(int, input().split())

# Please write your code here.


numbers = [i for i in range(1, n + 1)]

result = []


def recur(lev, start):
    if lev == m:
        print(*result)
        return

    for i in range(start, len(numbers)):
        result.append(numbers[i])
        recur(lev + 1, i + 1)
        result.pop()

    return


recur(0, 0)