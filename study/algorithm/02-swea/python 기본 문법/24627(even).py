arr = list(map(int, input().split()))

def find_even(arr):
    for i in arr :
        if i % 2 == 0 :
            return 1
        
    return 0

print(find_even(arr))