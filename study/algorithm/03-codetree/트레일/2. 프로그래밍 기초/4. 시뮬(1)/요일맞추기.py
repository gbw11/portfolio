m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
# m1, d1이 월요일 일때 m2, d2의 요일 계산

# 월별 요일 리스트
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day1 = 0
for i in range(m1):
    day1 += months[i]

day1 += d1

day2 = 0
for j in range(m2):
    day2 += months[j]

day2 += d2


dayweek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

print(dayweek[(day2 - day1) % 7])