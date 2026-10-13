import heapq
pq = []

heapq.heappush(pq, (2, 'BHC'))
heapq.heappush(pq, (1, 'NeNe'))
heapq.heappush(pq, (3, 'KFC'))
heapq.heappush(pq, (1, 'BBQ'))
heapq.heappush(pq, (2, 'Moms'))
heapq.heappush(pq, (4, 'Mc'))

while len(pq) > 1:
    num1, ch1 = heapq.heappop(pq)
    num2, ch2 = heapq.heappop(pq)
    ch = min(ch1, ch2)
    heapq.heappush(pq, (num1 + num2, ch))

num, ch = pq[0]

print(f'{ch} {num}')
