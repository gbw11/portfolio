arr =[]
while True:
    num = int(input())
    if num == 0:
        break
    arr.append(num)

R_arr =[]
for _ in range(len(arr)):
    R_arr.append(arr[-1])
    arr.pop(-1)

print(*R_arr, sep="")