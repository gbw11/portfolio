T = int(input())


def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    prev_dir = 0   # 0: 시작, -1: 왼쪽, 1: 오른쪽

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return True

        elif key < arr[mid]:
            if prev_dir == -1:   # 같은 방향 연속
                return False
            prev_dir = -1
            right = mid - 1

        else:  # key > arr[mid]
            if prev_dir == 1:    # 같은 방향 연속
                return False
            prev_dir = 1
            left = mid + 1

    return False

for tc in range(1, T+1):
    n , m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    result = 0

    for key in b:
        if  binary_search(a, key):
            result += 1

    print(f'#{tc}', result)