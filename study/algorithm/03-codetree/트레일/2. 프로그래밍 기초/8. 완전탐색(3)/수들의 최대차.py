n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

sort_arr = []

def get_arr(arr,minimum): # 최대최소의 차가 2 가되는 배열 형태 모두 구하는 함수
    maximum = minimum + k
    for idx, num in enumerate(arr):
        if num > maximum:
            arr[idx] = maximum
    sort_arr.append(arr)
    return 

while True:
    for i in arr:
        pass