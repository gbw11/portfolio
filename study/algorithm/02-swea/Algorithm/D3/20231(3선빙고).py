arr = []
for _ in range(5):
    arr.append(list(map(int, input().split())))


speak = []
for _ in range(5):
    speak.extend(map(int, input().split()))

for idx, num in enumerate(speak):

    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                arr[i][j] = 0

    bingo = 0

    for i in range(5):
        if arr[i].count(0) == 5 :
            bingo += 1

    for j in range(5):
        if sum(arr[i][j]==0 for i in range(5)) == 5:
            bingo += 1

    if all(arr[i][i] == 0 for i in range(5)):
        bingo += 1
        
    if all(arr[i][4 - i] == 0 for i in range(5)):
        bingo += 1

    if bingo >=3:
        print(num)
        break