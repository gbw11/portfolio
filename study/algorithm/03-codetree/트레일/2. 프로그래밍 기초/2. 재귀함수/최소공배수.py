n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a,b)


result = arr[0]
def recur(num = 1):
    global result
    if num == n:
        return result
    result = lcm(arr[num], result)
    return recur(num + 1)

print(recur())
