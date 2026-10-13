n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

result  = []

b = sorted(sequence)

for i in range(n):
    for j in range(n):
        if sequence[i] == b[j]:
            b[j] = 0 # 수열의 원소는 1이기 때문에 한번 체크한 거는 0
            result.append(j+1)
            break


print(*result)