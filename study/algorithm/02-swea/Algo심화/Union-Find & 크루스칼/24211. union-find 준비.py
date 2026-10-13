
parent = []
for i in range(8):
    parent.append(i)

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_b] = root_a

union(5, 6)
union(6, 7)
union(1, 2)

a, b = map(int, input().split())

print("O" if find(a)==find(b) else "X")