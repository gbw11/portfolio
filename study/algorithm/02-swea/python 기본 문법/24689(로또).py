a = {i for i in range(1,46)}

nums = list(map(int, input().split()))
for i in range(len(nums)):
    for j in range(1,len(nums)):
        if nums[i] == nums[j]:
            print("INVALID")

for num in nums:
    b = {i for i in range(1,46)}
    b.add(num)
    if b == a :
        continue
    else:
        print("INVALID")
        break
else:
    print("VALID")
    