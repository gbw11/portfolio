arr = [12, 3, 9, 1, 15, 7]

def counting_sort(arr):
    k = max(arr)
    counts = [0]*(k+1)
    temp = [0]*len(arr)

    for num in arr:
        counts[num] +=1

    for i in range(1,k+1):
        counts[i] += counts[i-1]
    
    for i in range(len(arr)-1,-1, -1):
        counts[arr[i]] -=1
        temp[counts[arr[i]]] = arr[i]

    return temp


# gpt 코드
'''
def counting_sort(arr):
    k = max(arr)
    counts = [0]*(k+1)

    for num in arr:
        counts[num] +=1

    result = []
    for idx, c in enumerate(counts):
        result.extend([idx]*c)

    return result
'''
print(*counting_sort(arr))
