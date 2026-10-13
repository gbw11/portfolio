abilities = list(map(int, input().split()))

# Please write your code here.

def get_diff(i, j, k):
    sum_1 = abilities[i] + abilities[j] + abilities[k]
    sum_2 = sum(abilities) - sum_1
    return abs(sum_1 - sum_2)

n = len(abilities)

result = float('inf')
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            result = min(result, get_diff(i,j,k))

print(result)