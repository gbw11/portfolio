n = int(input())

# Please write your code here.

result = []
cnt = 0
def find_beautynum(num):
    global cnt
    if num == n+1:
        i = 0
        while i < len(result):
            x = result[i]

            if i + x > len(result): # 범위 벗어나면
                return

            for j in range(i, i+x):
                if result[j] != x:
                    return
            i += x
        cnt += 1
        return

    for i in range(1, 5):
        result.append(i)
        find_beautynum(num +1)
        result.pop()

    return

find_beautynum(1)
print(cnt)