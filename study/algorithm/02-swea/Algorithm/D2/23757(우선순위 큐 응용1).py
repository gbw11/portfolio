import heapq
n = int(input())
pq = []

heapq.heappush(pq, (8, 'B'))
heapq.heappush(pq, (9, 'A'))
heapq.heappush(pq, (9, 'A'))
heapq.heappush(pq, (10, 'C'))
heapq.heappush(pq, (15, 'A'))



for _ in range(n):
    num, ch = heapq.heappop(pq)
    num = (num * 2) % 17
    heapq.heappush(pq, (num, ch))


sorted_arr = []

while pq:
    sorted_arr.append(heapq.heappop(pq))

for num, ch in sorted_arr:
    print(f'({num}, {ch})', end = ' ')