N, M = map(int, input().split())

# Please write your code here.

path = []

def recur(lev, start):
    if lev == M:
        print(*path)
        return

    for num in range(start, N+1):
        path.append(num)
        recur(lev+1, num+1)
        path.pop()

recur(0, 1)