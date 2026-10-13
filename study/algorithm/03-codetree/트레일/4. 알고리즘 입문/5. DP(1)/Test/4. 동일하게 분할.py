n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

total = sum(arr)

if total % 2 == 1:
    print("No")

else:
    target = total//2

    dp = [False]*(target+1)
    dp[0] = True

    for num in arr:
        for j in range(target,num-1,-1):
            if dp[j-num]:
                dp[j] = True

    if dp[target]:
        print("Yes")

    else:
        print("No")