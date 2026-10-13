n = int(input())

col = [False] * n
diag1 = [False] * (2 * n)
diag2 = [False] * (2 * n)

ans = 0


def dfs(row):
    global ans

    if row == n:
        ans += 1
        return

    for c in range(n):
        if not col[c] and not diag1[row + c] and not diag2[row - c + n]:
            col[c] = True
            diag1[row + c] = True
            diag2[row - c + n] = True

            dfs(row + 1)

            col[c] = False
            diag1[row + c] = False
            diag2[row - c + n] = False


dfs(0)

print(ans)