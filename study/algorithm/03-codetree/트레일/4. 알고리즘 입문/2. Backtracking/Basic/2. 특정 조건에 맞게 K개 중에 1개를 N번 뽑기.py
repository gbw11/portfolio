k, n = map(int, input().split())

# Please write your code here.


numbers = [i for i in range(1, k+1)]

path = []


def recur(lev):
    if lev == n:
        print(*path)
        return


    for num in numbers:
        if len(path)>=2 and path[-1]==num and path[-2]==num:
            continue
        path.append(num)
        recur(lev + 1)
        path.pop()

recur(0)
