def Find(parent, x):
    if x != parent[x]:
        parent[x] = Find(parent, parent[x])

    return parent[x]

def Union(parent, a, b):
    root_a = Find(parent, a)
    root_b = Find(parent, b)

    if root_a == root_b:
        return False

    parent[root_b] = root_a
    return True

def kruskal(v, edges, gender):
    parent = [i for i in range(v+1)]

    edges.sort(key=lambda x : x[2])

    mst_cost = 0
    mst_edges = []
    for a, b, cost in edges:
        if gender[a - 1] != gender[b - 1]:
            if Union(parent, a, b):
                mst_cost += cost
                mst_edges.append((a, b, cost))

    # 전체가 연결이 안되었으면 -1로 변경하기
    if len(mst_edges) != v-1:
        mst_cost = -1
    return mst_cost, mst_edges

n, m = map(int, input().split())
gender = list(input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

mst_cost, mst_edges = kruskal(n, edges, gender)
print(mst_cost)