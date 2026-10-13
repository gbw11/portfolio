d = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}

def Find(x):
    if parent[x] == x:
        return x
    return Find(parent[x])

def Union(a, b):
    root_a = Find(a)
    root_b = Find(b)

    if root_a != root_b:
        parent[root_b] = root_a

parent=[i for i in range(27)]

n = int(input())
for _ in range(n):
    a, b = input().split()
    a = d[a]
    b = d[b]
    Union(a, b)

# parent.sort()

res = []
for x in range(1, 27):
    res.append(Find(x))

res.sort()

ans = []
for i in range(25):
    if res[i]==res[i+1]:
       ans.append(res[i])
sub_ans = set(ans)
print(len(sub_ans))
print(26-len(sub_ans)-len(ans))

