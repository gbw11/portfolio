n = int(input())

# n개의 주사위를 던져서 합이 10이하가 되는 경우의 수 counting
'''
cnt = 0
result = []
def recur(num=0):
    global cnt
    if num == n:
        if sum(result)<=10:  # 전체를 다 만든 다음에 거른 비효율적인 방법
            cnt += 1
        return

    for i in range(1, 7):
        result.insert(num, i)
        recur(num+1)
        result.pop(num)

    return

recur()
print(cnt)
'''
# 가지치기를 이용한 방법
cnt = 0
result = []
def recur(num=0):
    global cnt
    if sum(result) > 10: # 가지치기를 활용!!
        return

    if num == n:
        cnt += 1
        return

    for i in range(1, 7):

        result.append(i)
        recur(num+1)
        result.pop()
    return

recur()
print(cnt)



