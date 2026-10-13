N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

# k 범위를 만들어와서 완전 탐색 진행해서 가장 큰 값 도출하기
result = 0

for i in range(min(arr), max(arr)+1):
    cnt = 0
    for num in arr:
        if i <= num <= i + K :
            cnt += 1
    
    result = max(result, cnt)

print(result)