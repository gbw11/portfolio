arrs = list(map(int, input().split()))

# Please write your code here.

arr = arrs[:] # 기존 리스트 기억하기 위해서 복사

result = []
for i in range(5):
    a = arr.pop(i)
    for j in range(4):
        for k in range(3):
            b = arr.pop(j)
            b += arr.pop(k)

            c = arr.pop()
            c += arr.pop()

            if a != b and b != c and c != a:
                result.append(max(a, b, c) - min(a, b, c))

                arr = arrs[:]

print(min(result))