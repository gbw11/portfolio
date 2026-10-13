text = input()
n = len(text)

result = 0
for idx, ch in enumerate(text):
    if ch=='[':
        last = text.find(']', idx+1)
        result += int(text[idx+1:last])
    elif ch=='{':
        last = text.find('}', idx+1)
        result *= int(text[idx+1:last])

print(result)