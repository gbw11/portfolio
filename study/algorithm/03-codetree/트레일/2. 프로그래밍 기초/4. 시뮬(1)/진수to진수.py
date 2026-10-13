a, b = map(int, input().split())
n = input()

# Please write your code here.

# n을 a진수에서 10진수로 바꾸기

decimal = 0
for digit in n:
    decimal = decimal*a + int(digit)


if decimal == 0:
    print(0)

else:
    res = ''
    while decimal > 0 :
        res = str(decimal % b) + res
        decimal //= b

    print(res)