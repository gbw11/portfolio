n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

maximum = arr[0]


def recur(num=1):
    global maximum

    if num == n:
        print(maximum)
        return

    maximum = max(maximum, arr[num])
    recur(num + 1)
    return


recur()