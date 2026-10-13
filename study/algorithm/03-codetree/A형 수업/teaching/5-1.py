'''
1 2 3 1 1 5
=> 1 1 5
=> 1 5
'''

n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

s1 -= 1
e1 -= 1
s2 -= 1
e2 -= 1

temp = [0 for _ in range(n)] # blocks와 같은 크기

last_idx = 0
for i in range(n):
    # 원본 배열을 조회 => 해당 위치에 값이 있으면 temp에 넣는다.
    if s1 <= i <= e1:
        continue

    temp[last_idx] = blocks[i] # 
    last_idx += 1

for i in range(n):
    blocks[i] = temp[i]


temp = [0 for _ in range(n)] # blocks와 같은 크기

last_idx = 0
for i in range(n):
    # 원본 배열을 조회 => 해당 위치에 값이 있으면 temp에 넣는다.
    if s2 <= i <= e2:
        continue

    temp[last_idx] = blocks[i]
    last_idx += 1

for i in range(n):
    blocks[i] = temp[i]

