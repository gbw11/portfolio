numbers = list(map(int, input().split()))

checked = 0
def is_babygin(arr):
    k = max(arr)
    counts = [0]*(k+1)

    global checked

    for num in arr:
        counts[num] +=1

    for i in range(len(counts)):
        if counts[i]>=3:
            counts[i] -=3
            checked +=1

    for i in range(len(counts)-2):
        if counts[i]>=1 and counts[i+1]>=1 and counts[i+2]>=1:
            counts[i] -=1
            counts[i+1] -=1
            counts[i+2] -=1
            checked +=1

    if checked ==2:
        return 'Yes'
    else:
        return 'No'

print(is_babygin(numbers))