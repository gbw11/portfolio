n = int(input())

# Please write your code here.


path = []
used = [0] * (n + 1)

def recur(lev):
    if lev == n:
        print(*path)
        return

    for i in range(1, n+1):
        if used[i] == 1: continue
        path.append(i)
        used[i] = 1
        recur(lev + 1)
        path.pop()
        used[i] = 0

    return

recur(0)