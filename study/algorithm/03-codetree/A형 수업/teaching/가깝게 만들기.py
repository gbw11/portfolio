from collections import deque
n, k = map(int, input().split())

arr = list(map(int, input().split()))

visited = [False] * (n+1)

result = float('inf')
def dfs(lev, ans):
    global result
    if lev == n:
        
        result = min(result, abs(k-ans))

        return 

    dfs(lev+1, ans+arr[lev])
    dfs(lev+1, ans-arr[lev])
    dfs(lev+1, ans*arr[lev])

dfs(1,arr[0])

print(result)