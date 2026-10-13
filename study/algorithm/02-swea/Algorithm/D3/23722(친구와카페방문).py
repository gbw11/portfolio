# friends = input().split()
#
# n = len(friends)
#
# # 2명 이상의 친구들과 같이 카페에 가는 경우의 수
#
# result = []
# cnt = 0
# def recur(idx=0):
#     global cnt
#     if idx == n: # n개 채우면 일단 무조건 끝내고
#         if sum(result) >= 2: # 그중에서 2명이상이면 세주기
#             cnt += 1
#         return
#
#     for i in range(2):
#         result.append(i)
#         recur(idx+1)
#         result.pop()
#     return
#
# recur()
# print(cnt)


#### binary counting 소스코드로 구현해보기

friends = input().split()

n = len(friends)


def get_sub(target):
    cnt = 0

    for i in range(n):
        if target & 0x1:
            cnt += 1

        target >>= 1
    if cnt >= 2: return 1
    else: return 0

result = 0
for i in range(1<<n):
    result += get_sub(i)

print(result)
