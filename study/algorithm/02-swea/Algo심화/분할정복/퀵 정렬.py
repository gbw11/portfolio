def quick_sort(arr):

    if len(arr) <= 1 :
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    result = quick_sort(left) + middle + quick_sort(right)

    return result

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = quick_sort(arr)
    print(f'#{tc}', ans[n//2])