'''
num = 827364
n = str(num)

even_cnt = (n.count("0") + n.count("2") +n.count("4") +
            n.count("6") +n.count("8"))

odd_cnt = (n.count("1") + n.count("3") +n.count("5") +
            n.count("7") +n.count("9"))

print(even_cnt)
print(odd_cnt)

#======================
# 전략 1번
num = str(num)
digit1 = int(num[0])
digit2 = int(num[1])
'''

#전략 2번
num = 827364
def get_count(num):
    digit1 = num // 100000
    digit2 = (num // 10000) % 10
    digit3 = (num // 1000) % 10
    digit4 = (num // 100) % 10
    digit5 = (num // 10) % 10
    digit6 = num % 10

    even_cnt = (digit1 % 2 == 0) + (digit2 % 2 == 0) +(digit3 % 2 == 0) + (digit4 % 2 == 0) + (digit6 % 2 == 0) + (digit6 % 2 == 0)
    odd_cnt = 6 - even_cnt
    return even_cnt , odd_cnt

even_cnt, odd_cnt = get_count(num)
print(even_cnt)
print(odd_cnt)

# 전략 3번(mod2)
# print((digit1 % 2==0) + (digit2 % 2 == 0))