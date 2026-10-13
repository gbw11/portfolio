arrs = list(map(int, input().split()))

# Please write your code here.

arr = arrs[:] # 기존 리스트 기억하기 위해서 복사

result = []
for i in range(5):
    a = arr[i]
    for j in range(5):
        for k in range(5):
            if i != j and j != k and k != i: 
                b = arr[j]
                b += arr[k]
                c = sum(arr) - (a+b)
            

            
                if a != b and b != c and c != a:
                    result.append(max(a, b, c) - min(a, b, c))

            

if result:
    print(min(result))

else: print(-1)