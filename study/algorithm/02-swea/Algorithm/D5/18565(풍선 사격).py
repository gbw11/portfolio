# T = int(input())
# for test_case in range(1, T+1):
n = int(input())
arr = list(map(int, input().split()))

max_score = 0
sum_score = 0

def dfs(arr, idx=1, sum_score):
    global max_score
    if sum_score < max_score:
        return

    if arr[idx-1]*arr[idx+1] > max_score:
        max_score
        sum_score
        return