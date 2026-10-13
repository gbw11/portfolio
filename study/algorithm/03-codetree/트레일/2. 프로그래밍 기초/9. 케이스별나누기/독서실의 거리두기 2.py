N = int(input())
seats = input()

# Please write your code here.

seat = [int(ch) for ch in seats]


# 완전 탐색으로 진행

def get_dis():
    dis = 1000
    for i in range(len(seat)):
        if seat[i] == 1:
            for j in range(i + 1, len(seat)):
                if seat[j] == 1:
                    dis = min(dis, j - i)
                    break
    return dis


result = 0
for i in range(N):
    if seat[i] == 0:
        seat[i] = 1
        result = max(result, get_dis())
        seat[i] = 0

print(result)