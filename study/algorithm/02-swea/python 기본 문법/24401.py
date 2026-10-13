arr = []
while True:
    num = int(input())
    if num == 0:
        arr.append(0)
        break
    arr.append(num)

j = 0
for i in range(len(arr)):
    
    if arr[i] <0:
        print(sum(arr[j:i]))
        j = i+1
    elif arr[i] == 0:
        print(sum(arr[j:]))
