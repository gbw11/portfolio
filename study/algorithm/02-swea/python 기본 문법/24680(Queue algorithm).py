friend = [1, 2, 3]
N = int(input())

for i in range(N):
    friend.append(friend[0])
    friend.pop(0)
print(friend[0])