n = int(input())
arr = list(input().split())

# Please write your code here.

b = sorted(arr)

cnt = 0
while True:
    for i in range(n):
        if arr[i] != b[i]:
            break #for문 탈출

    else: # 다 같으면 while문 탈출
        break

    for i in range(n-1): # 버블 정렬 코드
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            cnt += 1

print(cnt)