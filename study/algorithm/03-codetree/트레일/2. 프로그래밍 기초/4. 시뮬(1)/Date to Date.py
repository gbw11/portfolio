m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

if m1==m2:
    result = d2-d1+1
else:
    result = sum(month[m1+1:m2]) + (month[m1]-d1) + (d2) +1

print(result)