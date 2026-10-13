## 강사님 방법 하드코딩
arr = ["ABC", '77', '-33', '-33', '125', "ABC"]

d= dict()

for a in arr :
    d[a] = 0

for a in arr :
    d[str(a)] +=1

char = input()
print(d[char])

###

# arr = ["ABC", 77, -33, -33, 125, "ABC"]

# result = {}
# for ch in arr:
#     if ch not in result:
#         result[ch] = 0
#     result[ch] += 1

# text = input()
# print(result[text])