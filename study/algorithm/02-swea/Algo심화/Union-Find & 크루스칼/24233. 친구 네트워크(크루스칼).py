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
def Find(parent, x):
    if x != parent[x] :
        parent[x] = Find(parent, parent[x]) #경로 압축

    return parent[x]

def Union(parent, a, b):
    root_a = Find(parent, a)
    root_b = Find(parent, b)

    if root_a == root_b:
        return False

    parent[root_b] = root_a
    return True

def kruskal(v, edges):
    parent = [i for i in range(v+1)]

    edges.sort(key=lambda x: x[2])

    mst_cost = 0
    mst_edges = []

    for a, b, cost in edges:
        if Union(parent, a, b):
            mst_cost += cost
            mst_edges.append((a, b, cost))

    return mst_cost, mst_edges

m, n = map(int, input().split())

edges = []
for _ in range(m):
    a, b, c = input().split()
    a = d[a]
    b = d[b]
    c = int(c)
    edges.append((a, b, c))

mst_cost, mst_edges =kruskal(n, edges)
print(mst_cost)