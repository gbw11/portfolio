def Find(x):
    if parent[x] == x:
        return x
    return Find(parent[x])
def union(a, b):
    root_a = Find(a)
    root_b = Find(b)

    if root_a != root_b:
        parent[root_b] = root_a

parent = []
for i in range(30):
    parent.append(i)
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    union(a, b)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print("O" if Find(a)==Find(b) else "X")
