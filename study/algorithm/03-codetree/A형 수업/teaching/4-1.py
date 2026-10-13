a = [1,2,3,4,5]

temp = a[-1]

for i in range(len(a)-1, 0, -1):
    a[i] = a[i-1]

a[0] = temp




# 2차원에서
arr = []
tmp = arr[3][-1]

for i in range(len(arr[0]-1, 0, -1)):
    arr[3][i] = arr[3][i-1]

arr[3][0] = tmp

# for y in range(N):
#     for x in range(N):
#         arr[y][x]