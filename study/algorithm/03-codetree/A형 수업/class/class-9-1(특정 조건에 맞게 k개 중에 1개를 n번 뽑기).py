k, n = map(int, input().split())

# Please write your code here.

path = []

def recur(lev = 0):
    if lev == n:
        print(*path)
        return

    for num in range(1, k+1):
        if len(path)>=2 and num == path[-1] and num == path[-2]:
            continue
        path.append(num)
        recur(lev + 1)
        path.pop()

recur()