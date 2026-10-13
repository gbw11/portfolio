def Find(parent, x):
    if parent[x] != x:
        parent[x] = Find(parent, parent[x])
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

    edges.sort(key=lambda x : x[2])

    mst_cost = 0
    mst_edges = []
    for a, b, cost in edges:
        if Union(parent, a, b):
            mst_cost += cost
            mst_edges.append((a, b, cost))

    return mst_cost

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    x_pos = list(map(int, input().split()))
    y_pos = list(map(int, input().split()))
    # e :  터널의 세율
    e = float(input())

    edges = []
    for i in range(n):
        for j in range(n):
            dist = (x_pos[i]-x_pos[j])**2 + (y_pos[i]-y_pos[j])**2
            edges.append((i, j, e*dist))

    ans = kruskal(n, edges)
    print(f"#{tc}", round(ans))