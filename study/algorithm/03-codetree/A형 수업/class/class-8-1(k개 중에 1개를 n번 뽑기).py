k, n = map(int, input().split())

# Please write your code here.

path = []

def recur(lev):
    if lev == n:
        print(*path)
        return

    for i in range(1, k+1):
        path.append(i)
        recur(lev+1)
        path.pop()

recur(0)