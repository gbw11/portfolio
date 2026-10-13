n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

# 회색 : 0 , 흰색 : -1, 검정색 : 1

arr = [0 for _ in range(101)] # x값이 1부터 주어져서 0~ 100까지의  칸을 만듬

y = 50 #초기위치(정중앙)
for i in range(n):
    if dir[i] == 'L':
        for j in range(y, y-x[i], -1):
            arr[j] = -1
        y = y-x[i]+1 # 현재 위치로 바꾸기


    elif dir[i] == 'R':
        for j in range(y, y+x[i]):
            arr[j] = 1
        y = y+x[i]-1 # 현재 위치로 바꾸기

W = arr.count(-1)
B = arr.count(1)
print(W, B)