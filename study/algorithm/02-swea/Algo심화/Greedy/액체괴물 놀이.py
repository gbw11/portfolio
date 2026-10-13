n = int(input())

arr = list(map(int,input().split()))

arr.sort(reverse=True)
ans = 0
while len(arr) != 1:
    a = arr.pop()
    b = arr.pop()
    ans += (a+b)
    arr.append(a+b)
    arr.sort(reverse=True)


print(ans)