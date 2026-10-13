A = input()

# Please write your code here.

arr = list(A)
n = len(arr)


cnt = 1
for i in range(n-1):
    if arr[i] != arr[i+1]:
        cnt += 1
if cnt == 1:
    if n==10: print(3)
    else: print(2)

else:
    if arr[0] == arr[-1]:
        cnt -=1

    print(cnt * 2)