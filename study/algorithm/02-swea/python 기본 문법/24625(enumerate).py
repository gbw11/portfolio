number = list(map(int, input().split()))


max_idx = 0
for idx, num in enumerate(number):
    if num > number[max_idx]:
        max_idx = idx
    
print(max_idx)
