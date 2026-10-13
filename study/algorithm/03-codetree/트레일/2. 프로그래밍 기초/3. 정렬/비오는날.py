n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.

idx = -1
mini = '9999-12-31'
for i in range(n):
    if weather[i] == 'Rain':
        if date[i] < mini:  # 문자열이어도 자릿수가 같다면 크기 비교 가능!!
            mini = date[i]
            idx = i

print(date[idx], day[idx], weather[idx])

