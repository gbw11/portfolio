def merge_sort(arr):
    global cnt
    # 남은 배열의 길이가 1 이하이면 이미 정렬된 것으로 간주하고 반환
    if len(arr) <= 1:
        return arr
    # 배열을 반으로 나눈다
    mid = len(arr) // 2
    # 왼쪽 절반을 재귀적으로 정렬
    left = merge_sort(arr[:mid])
    # 오른쪽 절반을 재귀적으로 정렬
    right = merge_sort(arr[mid:])
    # 병합: 정렬된 왼쪽과 오른쪽 배열을 병합
    result = merge(left, right)

    return result # 정렬된 배열

def merge(left, right):
    global cnt
    result = []
    # 왼쪽과 오른쪽 인덱스
    i, j = 0, 0
    # 왼쪽과 오른쪽 배열을 비교하면서 병합

    if left[-1] > right[-1]: cnt += 1

    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # 왼쪽 요소가 작거 같으면
            result.append(left[i]) # 작은게 append
            i += 1 # 인덱스가 다음 요소로 이동
        else: # 오른쪽 요소가 작으면
            result.append(right[j])
            j += 1 # 인덱스가 다음 요소로 이동

    # 왼쪽 배열에 남은 요소들 extend로 추가
    result.extend(left[i:])
    # 오른쪽 배열에 남은 요소들 extend로 추가
    result.extend(right[j:])

    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    sorted_arr = merge_sort(arr)
    print(f'#{tc} {sorted_arr[N//2]} {cnt}')