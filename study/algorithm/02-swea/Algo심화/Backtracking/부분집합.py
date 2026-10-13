arr = [1,2,3,4,5,6,7,8,9,10]


path = []

def dfs(start):
    if sum(path)>=10:
        if sum(path)==10:
            print(*path)

    for i in range(start, len(arr)):
        path.append(arr[i])
        dfs(i+1)
        path.pop()

dfs(0)