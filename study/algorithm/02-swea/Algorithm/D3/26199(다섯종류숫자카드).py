# 다섯종류의 숫자카드 입력 받음
# 다섯개 중에 4개 뽑음
# 뽑을때마다 전에 뽑았던 카드번호와 간격이 3 이하로 차이나는 중복 순열?
'''
numbers = [int(ch) for ch in input()]


result = []
cnt = 0
def recur(n=0):
    global cnt
    if n==4:
        for i in range(3):
            if abs(result[i] - result[i+1])>3:
                break
        else: cnt += 1
        return


    for num in numbers:
        result.append(num)
        recur(n+1)
        result.pop()
    return
recur()
print(cnt)
'''

### 중복순열로 해결하기

numbers = [int(ch) for ch in input()]


result = []
cnt = 0

def recur(lev):
    global cnt


    if lev==4:
        cnt += 1
        return

    for num in numbers:
        if result and abs(result[-1] - num)>3:
            continue
        result.append(num)
        recur(lev + 1)
        result.pop()
    return

recur(0)
print(cnt)